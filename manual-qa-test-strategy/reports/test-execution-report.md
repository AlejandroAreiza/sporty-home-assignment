# Test Execution Report - Single Bet Placement

Results of the test execution sessions defined in the [Test Plan](../test-plan/test-plan-single-bet-placement.md#35-test-execution-sessions). Bug details are in [bug-reports.md](bug-reports.md).

## Session Details

| Item | Value |
|------|-------|
| Tester | Alejandro Areiza |
| Application | https://qae-assignment-tau.vercel.app/ |
| User ID | `candidate-ZrzbrQMxczHo` |
| Browser | Latest desktop Chrome |

## Summary

| Activity | Executed | Passed | Failed | Not executed | Bugs found |
|----------|----------|--------|--------|--------------|------------|
| Scripted testing | 3 test cases | 0 | 3 | 2 | 7 |
| Exploratory testing | 9 checks | 6 | 3 | - | 3 |
| **Total** | | | | | **9 unique bugs** (2 Critical, 5 High, 2 Low) |

BUG-09 was found in both scripted (TC-03) and exploratory testing, so it is counted once in the total.

## Scripted Testing Results

| Test Case | Test Priority | Test Execution Status | Bugs Found |
|-----------|----------|--------|------|
| **TC-01** Place a valid single bet on an upcoming match | Critical | ❌ Fail | [BUG-02](bug-reports.md#bug-02), [BUG-03](bug-reports.md#bug-03), [BUG-04](bug-reports.md#bug-04), [BUG-05](bug-reports.md#bug-05) |
| **TC-03** Reject a bet when the stake exceeds the available balance | Critical | ❌ Fail | [BUG-09](bug-reports.md#bug-09) |
| **TC-02** Enforce the maximum stake boundary via the API | High | ❌ Fail | [BUG-06](bug-reports.md#bug-06), [BUG-07](bug-reports.md#bug-07) |
| **TC-04** Reject bets on past matches via the API | High | Not executed | - |
| **TC-05** Double submit does not place duplicate bets | High | Not executed | - |

## Exploratory Testing Notes

**Charter:** explore the match list filters and the bet placement flow to find issues the scripted test cases miss.

| Area | Layer | What was checked | Result | Bugs Found |
|------|-------|------------------|--------|------------|
| Balance reset | API + UI | Reset the balance and compare the response with `GET /api/balance` and the header | ❌ Fail | [BUG-01](bug-reports.md#bug-01) |
| Date filter | UI | Filter the match list by a single date | ✅ Pass | - |
| Odds filter | UI | Filter the match list by an odds range | ✅ Pass | - |
| Match count label | UI | Label after filtering | ❌ Fail | [BUG-08](bug-reports.md#bug-08) |
| Stake input validation | UI | Enter `0`, `-5`, `0.99`, `100.01`, `1.005`, `1,50`, letters and spaces | ✅ Pass | - |
| Change selection | UI | Select `1`, then `X`, then `2` on the same match | ✅ Pass: the new selection replaces the previous one and the bet slip updates | - |
| Single selection only | UI | Select odds on one match, then on another match | ✅ Pass: only one selection at a time; no multi-selection allowed | - |
| Remove selection | UI | Remove the selection from the bet slip (`x` and `Remove All`) | ✅ Pass: the selection is cleared from the bet slip and the match list | - |
| Repeated bets | API | Send several `POST /api/place-bet` requests (`stake: 100`) rapidly, then slowly one after another | ❌ Fail: rapid requests are cancelled by the API client (`REQUEST_CANCELLED`), so they never reach the server. Slow requests are all accepted: 7 × `200 OK` with `stake: 100` in about 12 seconds, far more than the €120.00 balance allows| [BUG-09](bug-reports.md#bug-09) |
