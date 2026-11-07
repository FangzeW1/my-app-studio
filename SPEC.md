# App Studio decisions

The durable agreement between learner and AI. Update only agreed decisions and
actual evidence; pending is a valid state. Keep explanations/help in
[LEARNING.md](LEARNING.md), not a second copy here.

## Current stage

- **Current feature:** APP-003.
- **Status:** APP-001, APP-002 and APP-003 kept; each issue closed and its PR merged. Latest PR and merged-main check/windows jobs passed for each lesson. All learner checkpoints reviewed and approved.
- **Next step:** Submit the repository and the three linked lesson PRs.
- **Implementation marker:** APP-003 (3), advanced only after full cumulative checks passed.

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
| One visible choice and visitor benefit | Clean blue/white design; learner predicts easier organization and lower stress. Learner found the headline and clean layout approachable and communicating less overwhelming schoolwork. |
| Own issue / branch / PR | [Issue #1](https://github.com/FangzeW1/my-app-studio/issues/1) / `codex/app-001-tasknest` / [PR #2](https://github.com/FangzeW1/my-app-studio/pull/2) |

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
| Expected public/private behavior and account flow | Signup/login/private dashboard/logout; anonymous dashboard requests redirect to login, successful login grants access, logout revokes access. Prepared password hashing and session protections; storage excluded. |
| Valid and rejected cases to demonstrate | Valid signup/login; duplicate or invalid signup, role injection, bad login, anonymous private access, missing CSRF and copied-token replay after logout rejected. |
| Own issue / branch / PR | [Issue #3](https://github.com/FangzeW1/my-app-studio/issues/3) / `codex/app-002-accounts` / [PR #4](https://github.com/FangzeW1/my-app-studio/pull/4) |

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
| Intended admin-only result | A small admin-only permission confirmation page and API; anonymous users log in, members receive 403, admins allowed. Role changes only through trusted local CLI and effective for existing sessions. |
| Actual allowed/denied request evidence | Isolated browser/API review: anonymous admin API 401; same logged-in session member 403, promoted admin 200, downgraded member 403. Trusted CLI used for role changes. |
| Own issue / branch / PR | [Issue #5](https://github.com/FangzeW1/my-app-studio/issues/5) / `codex/app-003-roles` / [PR #6](https://github.com/FangzeW1/my-app-studio/pull/6) |

**Keep when:** a direct request cannot bypass the role boundary, role changes
take effect as specified, new signup remains member-only, and full cumulative
checks plus AI review pass. Link the learner's actual interpretation/observation,
reviewed record and verified GitHub result. Hidden navigation alone is insufficient.

## Evidence

Link actual files/checks and the student's own issues/PRs. No fabricated URLs,
customer research or claims that a timestamp proves learning.

| Feature | Files / own issue / PR | Actual checks and learner observations | Kept / GitHub state |
|---|---|---|---|
| APP-001 | `app/brand.json`, homepage/base templates, shared CSS and SVG; [issue #1](https://github.com/FangzeW1/my-app-studio/issues/1), [PR #2](https://github.com/FangzeW1/my-app-studio/pull/2) | Both full APP-001 runs passed; desktop/narrow reviewed; learner interpretation, browser observation and keep reason in LEARNING.md | Kept; PR #2 merged, issue #1 closed; PR and main check/windows passed |
| APP-002 | `app/features/accounts.py`, `app/templates/account.html`, `app/templates/dashboard.html`; [issue #3](https://github.com/FangzeW1/my-app-studio/issues/3), branch `codex/app-002-accounts`, [PR #4](https://github.com/FangzeW1/my-app-studio/pull/4) | Full cumulative checks: Black/Pylint, 98 foundation tests, 14 contracts, 2 Chromium journeys passed. Desktop/narrow account pages reviewed; learner accessed Member space after login and was redirected to login after logout. | Kept; PR #4 merged; issue #3 closed; PR CI 42334872883 and main CI 42335008631 check/windows passed |
| APP-003 | `app/features/roles.py`, `app/templates/admin.html`, shared CSS, `contracts/test_roles.py`; [issue #5](https://github.com/FangzeW1/my-app-studio/issues/5), branch `codex/app-003-roles`, [PR #6](https://github.com/FangzeW1/my-app-studio/pull/6) | Black/Pylint, 98 foundation tests, 19 cumulative contracts and 2 Chromium journeys passed. Actual denied/allowed desktop and 390px layouts reviewed, no horizontal overflow. | Kept; PR #6 merged as cfaae50, issue #5 closed; PR CI 42336722431 and merged-main CI 42336879139 check/windows passed |

The instructor's reference branches show possible implementations. They do not
establish this repository's completion or the learner's own reasoning.

## Verified completion links

| Lesson | Latest PR CI (check/windows passed) | Merged-main CI (check/windows passed) | Merge |
|---|---|---|---|
| APP-001 | [Run 42332653472](https://github.com/FangzeW1/my-app-studio/actions/runs/42332653472) | [Run 42332849036](https://github.com/FangzeW1/my-app-studio/actions/runs/42332849036) | 71e1134 |
| APP-002 | [Run 42334872883](https://github.com/FangzeW1/my-app-studio/actions/runs/42334872883) | [Run 42335008631](https://github.com/FangzeW1/my-app-studio/actions/runs/42335008631) | 56c6b7b |
| APP-003 | [Run 42336722431](https://github.com/FangzeW1/my-app-studio/actions/runs/42336722431) | [Run 42336879139](https://github.com/FangzeW1/my-app-studio/actions/runs/42336879139) | cfaae50 |

Local main was updated from origin after every lesson merge. Final cumulative local
checks passed Black, Pylint, 98 foundation tests, 19 contracts and 2 real Chromium
journeys. Learner evidence and AI assistance are recorded in LEARNING.md.
Assignment storage and production deployment remain outside the agreed scope.
