# App Studio decisions

The durable agreement between learner and AI. Update only agreed decisions and
actual evidence; pending is a valid state. Keep explanations/help in
[LEARNING.md](LEARNING.md), not a second copy here.

## Current stage

- **Current feature:** APP-001.
- **Status:** TaskNest homepage implemented; full APP-001 checks passed; learner inspection and keep decision received; evidence accuracy approved; GitHub cycle pending.
- **Next step:** Publish the PR and verify both CI jobs before merging.
- **Implementation marker:** `studio.json`: `implemented_through: 1` after full APP-001 checks passed.

This repository owns application code. Server/proxy changes and production
deployment are outside these three local-development lessons. Prepared helpers
are reusable foundations, not evidence that unfinished routes are implemented.

## APP-001 · Branded homepage

**Scope:** make the neutral FastAPI homepage express one chosen identity with
a simple original SVG mark, coherent copy, navigation and shared style tokens.
Keep account actions honest about their unfinished state.

| Decision | Agreement |
|---|---|
| Visitor and concrete use situation | Students managing assignments and projects |
| Reused IS117 brand, or name / promise / primary archetype | TaskNest / schoolwork organized in one place / Caregiver |
| One visible choice and visitor benefit | Clean blue/white design; learner predicts easier organization and lower stress. Homepage audience effect not yet observed. |
| Own issue / branch / PR | Pending |

**Keep when:** the agreed identity is visible and usable at desktop/narrow widths;
full foundation + APP-001 checks pass; AI review and the learner's actual check
interpretation/browser observation/keep reason are recorded; reviewed evidence
and verified GitHub state are linked below.

## APP-002 · Signup, login and logout

**Scope:** add browser forms and REST behavior for member signup, login, a private
dashboard and logout backed by SQLite. Reuse the prepared password/JWT/CSRF/session
helpers; keep data local. New accounts cannot choose their role.

| Decision | Agreement |
|---|---|
| Expected public/private behavior and account flow | Pending |
| Valid and rejected cases to demonstrate | Pending |
| Own issue / branch / PR | Pending |

**Keep when:** the agreed forms/API work; duplicate/invalid signup and wrong
credentials are rejected; passwords are hashed; authentication uses validated,
expiring JWTs with protected cookies and CSRF; private requests require a live
session and logout revokes it. Full cumulative checks, AI review, actual learner
contributions and GitHub state are recorded. This is not a production-security certification.

## APP-003 · Server-enforced roles

**Scope:** enforce a small member/admin boundary in the API and browser. Assign
roles only through the trusted local terminal command; use current server-side
permissions, including for an existing session after a role change.

| Visitor | Homepage | Member area | Admin area/API |
|---|---|---|---|
| Anonymous | Allowed | Login required | Login required |
| Member | Allowed | Allowed | Forbidden |
| Admin | Allowed | Allowed | Allowed |

| Decision | Agreement |
|---|---|
| Intended admin-only result | Pending |
| Actual allowed/denied request evidence | Pending |
| Own issue / branch / PR | Pending |

**Keep when:** a direct request cannot bypass the role boundary, role changes
take effect as specified, new signup remains member-only, and full cumulative
checks plus AI review pass. Link the learner's actual interpretation/observation,
reviewed record and verified GitHub result. Hidden navigation alone is insufficient.

## Evidence

Link actual files/checks and the student's own issues/PRs. No fabricated URLs,
customer research or claims that a timestamp proves learning.

| Feature | Files / own issue / PR | Actual checks and learner observations | Kept / GitHub state |
|---|---|---|---|
| APP-001 | Pending | Not run; learner contributions pending | Pending |
| APP-002 | Pending | Unfinished; explicit contracts not yet passed | Pending |
| APP-003 | Pending | Unfinished; explicit contracts not yet passed | Pending |

The instructor's reference branches show possible implementations. They do not
establish this repository's completion or the learner's own reasoning.

### APP-001 working agreement

- Identity: TaskNest, for students managing assignments and projects; promise: keep schoolwork organized in one place.
- Primary archetype: Caregiver; supportive and reliable. Clean blue-and-white design and an original nest-and-check SVG mark.
- Scope: homepage, copy, navigation and shared styles. Accounts, assignment tracking and project storage remain unavailable.
- Issue: https://github.com/FangzeW1/my-app-studio/issues/1
- Branch: `codex/app-001-tasknest`; PR pending.
- Files: `app/brand.json`, `app/templates/home.html`, `app/templates/base.html`, `app/static/site.css`, `app/static/logo.svg`.
- Baseline: Black, Pylint, 98 non-browser tests and 2 Chromium journeys passed. Full APP-001: Black, Pylint, 98 foundation tests, 2 homepage contracts and 2 Chromium journeys passed. Desktop (1440px) and narrow (390px) renders reviewed without horizontal overflow; Learner described the approachable headline/blue-white design and accepted section-only navigation for APP-001; keep authorized. Evidence accuracy approved before publication.
