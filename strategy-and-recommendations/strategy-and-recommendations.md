# Strategy & Recommendations

## Why These 2 Tests Were Automated

| Test | Layer | Why it was chosen |
|------|-------|-------------------|
| [TC-01](../manual-qa-test-strategy/test-plan/test-plan-single-bet-placement.md#tc-01) Place a valid single bet on an upcoming match | E2E UI | It is the **core money flow** and the main user journey. It checks every step a user sees (bet slip, stake, Place Bet, receipt, balance), so one test protects the most business value. It catches 3 Critical/High bugs on every run: receipt team order ([BUG-02](../manual-qa-test-strategy/reports/bug-reports.md#bug-02)), receipt payout ([BUG-03](../manual-qa-test-strategy/reports/bug-reports.md#bug-03)) and balance not updated ([BUG-04](../manual-qa-test-strategy/reports/bug-reports.md#bug-04)). |
| [TC-02](../manual-qa-test-strategy/test-plan/test-plan-single-bet-placement.md#tc-02) Verify the API enforces the maximum stake | API | A stake above the maximum is a **financial risk**, and only a direct API call proves the backend enforces the limit (the UI can be bypassed). It uses boundary values (€100.00 accepted, €100.01 rejected) and checks the full response, catching the wrong currency ([BUG-07](../manual-qa-test-strategy/reports/bug-reports.md#bug-07)). The maximum was chosen over the minimum because the spec is clear on €100.00, while the minimum is contradictory (€1.00 vs €1.01). |

Together they cover both layers: the **UI** (what the user sees) and the **API** (what the backend enforces).

## What Was Left Manual Only

| Scenario | Why it stays manual |
|----------|---------------------|
| [TC-05](../manual-qa-test-strategy/test-plan/test-plan-single-bet-placement.md#tc-05) Double submit | The result depends on click timing and network speed, so an automated UI check would pass or fail at random (flaky). A tester can slow the network and record evidence. |
| Receipt shows the selection ([BUG-05](../manual-qa-test-strategy/reports/bug-reports.md#bug-05)) | The receipt has no element for the selection, so there is nothing reliable to locate yet. |
| Exploratory checks (filters, match count label, stake input formats) | Low risk, or exploratory by nature. They are documented in the [execution report](../manual-qa-test-strategy/reports/test-execution-report.md#exploratory-testing-notes). |


## Recommendations

1. **CI/CD pipeline - Git Actions:** Run lint and API tests on every pull request (fast, no browser), and UI tests headless on merge and nightly. Publish the Allure report as a build artifact. Add Selenium Grid in Docker when parallel or cross-browser runs are needed.
2. **Test data manager:** Give each test run its own user, and fix the reset endpoint, so every test starts from a known balance. Move test data (stake boundaries, odds) into JSON/YAML files, and add a fixed-data regression test for the odds-dependent payout.
3. **Makefile:** One short command per task (`make install`, `make test`, `make api`, `make ui`, `make report`, `make lint`), so local runs and the CI pipeline use the same commands and new team members don't need to remember pytest flags.
4. **Video in the Allure report:** Record every UI test run (e.g. Selenium Grid video container) and attach the video, plus a screenshot on failure, to the Allure report. A failed run then shows exactly what happened, which saves time reproducing flaky or timing-related bugs.
5. **Claude Code with project skills:** Add a `CLAUDE.md` with the framework conventions (Screenplay layers, locator priority, no sleeps, hard vs soft asserts) and skills that read a feature spec and generate, out of the box:
   - a **test plan** with risk-based, prioritized test cases (same template as the [test plan](../manual-qa-test-strategy/test-plan/test-plan-single-bet-placement.md)),
   - the **automation**: new steps, questions, page elements and pytest tests that follow the framework structure.

   The output is reviewed by a QA engineer before it is merged, so the team writes less boilerplate and spends more time on exploratory testing and risk analysis.
