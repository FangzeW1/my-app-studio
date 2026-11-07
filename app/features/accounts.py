"""APP-002 browser forms and REST routes share prepared account services."""

from typing import Annotated

from fastapi import APIRouter, Depends, Header, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from pydantic import ValidationError

from app import security
from app.schemas import LoginInput, PublicUser, SignupInput

router = APIRouter()


def _csrf(request: Request, x_csrf_token: Annotated[str | None, Header()] = None):
    """Guard JSON state changes with the session's synchronizer token."""
    security.require_csrf(request, x_csrf_token)


def _register(request: Request, credentials: SignupInput):
    """Use the same throttled member-only signup service from forms and JSON."""
    security.limit_signup(request)
    return security.signup(
        request.app.state.settings, credentials.username, credentials.password
    )


def _sign_in(request: Request, response: Response, credentials: LoginInput):
    """Use the same password verification and session rotation for both clients."""
    return security.login(request, response, credentials.username, credentials.password)


def _page(request: Request, name: str, *, status=200, **context):
    """Render forms with a CSRF token without exposing credentials or session data."""
    cookies = Response()
    token = security.csrf_token(request, cookies)
    response = request.app.state.templates.TemplateResponse(
        request=request,
        name=name,
        context={"csrf_token": token, **context},
        status_code=status,
    )
    response.raw_headers.extend(
        (key, value) for key, value in cookies.raw_headers if key == b"set-cookie"
    )
    return response


@router.get("/api/csrf")
def api_csrf(request: Request, response: Response):
    """Provide the pre-login or current session's same-origin CSRF token."""
    return {"csrf_token": security.csrf_token(request, response)}


@router.post(
    "/api/signup",
    status_code=201,
    response_model=PublicUser,
    dependencies=[Depends(_csrf)],
)
def api_signup(request: Request, credentials: SignupInput):
    """Create only members and return only public identity fields."""
    return _register(request, credentials)


@router.post("/api/login", response_model=PublicUser, dependencies=[Depends(_csrf)])
def api_login(request: Request, response: Response, credentials: LoginInput):
    """Authenticate through a protected cookie rather than a JSON bearer token."""
    return _sign_in(request, response, credentials)


@router.get("/api/me", response_model=PublicUser)
def api_me(user: Annotated[dict, Depends(security.require_user)]):
    """Require a live validated session for the current public identity."""
    return user


@router.post("/api/logout", dependencies=[Depends(_csrf)])
def api_logout(request: Request, response: Response):
    """Revoke server-side state before removing the cookie."""
    security.logout(request, response)
    return {"detail": "Logged out."}


@router.get("/signup")
def signup_page(request: Request):
    """Show the accessible member signup form."""
    return _page(request, "account.html", signup=True, username="", error=None)


@router.get("/login")
def login_page(request: Request):
    """Show the accessible login form."""
    return _page(request, "account.html", signup=False, username="", error=None)


async def _submit(request: Request, *, signup: bool):
    """Validate all fields and retain only a validated username after an error."""
    username = ""
    try:
        async with request.form(max_fields=3, max_files=0, max_part_size=2048) as form:
            security.require_csrf(request, form.get("csrf_token"))
            fields = dict(form)
            fields.pop("csrf_token", None)
            model = SignupInput if signup else LoginInput
            credentials = model.model_validate(fields)
        username = credentials.username
        if signup:
            _register(request, credentials)
            return RedirectResponse("/login", status_code=303)
        response = RedirectResponse("/dashboard", status_code=303)
        _sign_in(request, response, credentials)
        return response
    except ValidationError:
        return _page(
            request,
            "account.html",
            status=422,
            signup=signup,
            username="",
            error="Check your username and password requirements and try again.",
        )
    except HTTPException as error:
        response = _page(
            request,
            "account.html",
            status=error.status_code,
            signup=signup,
            username=username,
            error=error.detail,
        )
        if error.headers:
            response.headers.update(error.headers)
        return response


@router.post("/signup")
async def signup_form(request: Request):
    """Submit the same member-only operation as the REST route."""
    return await _submit(request, signup=True)


@router.post("/login")
async def login_form(request: Request):
    """Submit the same guarded login operation as the REST route."""
    return await _submit(request, signup=False)


@router.get("/dashboard")
def dashboard(request: Request):
    """Redirect anonymous visitors and render a private member greeting."""
    user = security.authenticate(request)
    if user is None:
        return RedirectResponse("/login", status_code=303)
    return _page(request, "dashboard.html", user=user)


@router.post("/logout")
async def logout_form(request: Request):
    """Only a CSRF-protected POST can revoke the browser's session."""
    async with request.form(max_fields=1, max_files=0, max_part_size=2048) as form:
        security.require_csrf(request, form.get("csrf_token"))
    response = RedirectResponse("/login", status_code=303)
    security.logout(request, response)
    return response
