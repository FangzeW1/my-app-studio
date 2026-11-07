"""APP-003 guards admin HTML and API requests using current server permissions."""

from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse

from app import security
from app.schemas import PublicUser

router = APIRouter()


@router.get("/api/admin", response_model=PublicUser)
def admin_api(user: Annotated[dict, Depends(security.require_admin)]):
    """Return a permission confirmation only after the current admin guard passes."""
    return user


@router.get("/admin")
def admin_page(request: Request):
    """Apply the same guard to typed URLs as to requests from the admin link."""
    try:
        user = security.require_admin(request)
    except HTTPException as error:
        if error.status_code == 401:
            return RedirectResponse("/login", status_code=303)
        if error.status_code != 403:
            raise
        return request.app.state.templates.TemplateResponse(
            request=request,
            name="admin.html",
            context={"user": None},
            status_code=403,
        )
    return request.app.state.templates.TemplateResponse(
        request=request, name="admin.html", context={"user": user}
    )
