# Conversation evidence

AI-drafted task summary, not a transcript or grade. It may be public. Use actual
short words or labeled paraphrases; disclose help and leave missing responses
pending. The learner reviews, corrects or removes new excerpts before commit/push.
Accuracy approval is not proof of understanding. Label simulated trials explicitly.

**Available conversation context:** This chat, from local onboarding through the current APP-001 work; no earlier learner conversation is available.

## APP-001

- Prediction: Learner paraphrase: Easier access to schoolwork, clearer assignment priorities and cleaner organization could make work easier to handle and lower stress.
- Check interpretation: Learner paraphrase: The 390px check catches elements extending beyond the screen and unwanted horizontal scrolling. It does not prove readability, working buttons or correct layout at other screen sizes.
- Browser observation: Initial neutral page, learner paraphrase: Noticed the headline A small idea. A real application. in massive print. TaskNest observation (learner paraphrase): The large headline A little order. More room to breathe and clean blue/white layout feel approachable and communicate less overwhelming schoolwork. Buttons navigate homepage sections; acceptable for APP-001 because accounts and other functionality belong to later lessons.
- Keep decision: Learner paraphrase: Keep this implementation; the approachable design communicates the intended benefit and section-only buttons fit APP-001. Learner authorized the PR, CI checks and merge.
- Review: Learner approved the presented excerpts for publication as accurate before commit/push, and requested that the prediction remain grounded in their actual words. The prediction paraphrases their earlier reply about finding work, assignment priorities, cleaner organization and lower stress.
- Help/gaps: Learner chose TaskNest, student assignments/projects, an organization promise, Caregiver support/reliability and blue/white styling. AI wrote the homepage copy, SVG and styles. Prediction describes the intended app benefit; the homepage alone does not demonstrate organization or stress reduction. AI ran both full APP-001 check commands and reviewed desktop/narrow renders. Learner supplied the check interpretation, TaskNest browser observation and keep decision. Learner approved record accuracy. PR #2 verified merged, issue #1 verified closed, and latest PR/main check and windows jobs passed.
- Evidence links / next step: Issue https://github.com/FangzeW1/my-app-studio/issues/1; branch codex/app-001-tasknest. Both full APP-001 runs passed (98 foundation tests, 2 contracts, 2 Chromium journeys, Black and Pylint). Committed and pushed as 13d6b8b; PR https://github.com/FangzeW1/my-app-studio/pull/2. Verified merge 71e1134, issue #1 closed, latest PR CI 42332653472 and main CI 42332849036 both check/windows successful. Next: agree APP-002 scope.

## APP-002

- Prediction: Learner paraphrase: Before login the dashboard should deny access and redirect to login; after successful login it should allow the authenticated user. Logout should prevent access until another login.
- Check interpretation: Learner paraphrase: The replay test catches logout failing to invalidate the session and an old cookie still accessing private information. A 401 shows the copied cookie can no longer authenticate after logout.
- Browser observation: Learner paraphrase: Created an account, logged in and accessed Member space. After logout, reopening Member space redirected to the login page.
- Keep decision: Learner approved keeping APP-002 because the observed redirect demonstrates that logged-out users cannot access the private dashboard; authorized commit, PR, CI verification, merge and issue closure.
- Review: Learner approved all presented APP-002 prediction, interpretation, observation, keep and help/gaps entries as accurate before publication.
- Help/gaps: Learner approved signup/login/private dashboard/logout with prepared helpers, hashed passwords and no assignment storage. AI connected forms and API to prepared helpers and explained password hashing, signed expiring JWTs (signature is not encryption), HttpOnly cookies and server-side revocation. Learner interpreted the actual copied-cookie replay test. Learner completed browser inspection, approved keeping the result and approved the new record for publication. GitHub completion pending.
- Evidence links / next step: Issue https://github.com/FangzeW1/my-app-studio/issues/3; branch codex/app-002-accounts. Full cumulative APP-002 checks passed: Black/Pylint, 98 foundation tests, 14 contracts and 2 Chromium journeys. AI reviewed actual signup/dashboard desktop/narrow renders with no horizontal overflow. Normal full recheck also passed; learner checkpoints completed and approved. PR/CI/merge pending.

## APP-003

- Prediction: Pending.
- Check interpretation: Pending.
- Browser observation: Pending.
- Keep decision: Pending.
- Review: Pending.
- Help/gaps: Pending.
- Evidence links / next step: Keep APP-002 before agreeing this lesson.
