# Test Plan - Single Bet Placement

## Table of Contents
- [Test Plan - Single Bet Placement](#test-plan---single-bet-placement)
  - [Table of Contents](#table-of-contents)
  - [1. Introduction](#1-introduction)
    - [1.1 Objectives](#11-objectives)
    - [1.2 Scope](#12-scope)
    - [1.3 Out Of Scope](#13-out-of-scope)
    - [1.4 System Overview](#14-system-overview)
    - [1.5 Definitions/Acronyms](#15-definitionsacronyms)
  - [2. Approach](#2-approach)
    - [2.1 Assumptions](#21-assumptions)
    - [2.2 Test Coverage](#22-test-coverage)
    - [2.3 Test Tools](#23-test-tools)
    - [2.4 Test Type](#24-test-type)
  - [3. Test Execution](#3-test-execution)
    - [3.1 Test Environment](#31-test-environment)
    - [3.2 Test Cases Attributes](#32-test-cases-attributes)
    - [3.3 Bug Attributes](#33-bug-attributes)
    - [3.4 Test Cases](#34-test-cases)
    - [3.5 Test Execution Sessions](#35-test-execution-sessions)
      - [3.5.1 Scripted Testing](#351-scripted-testing)
      - [3.5.2 Exploratory Testing](#352-exploratory-testing)

## 1. Introduction

This test plan describes how the **Single Bet Placement feature** will be tested. It describes scope, test approach, test environment, test scenarios, and how results and defects are reported.

Testing is **risk-based**: it focuses on the areas where a failure would hurt users or the business most, which are money, bet integrity and validation. The goal is strong coverage of high-risk behavior, not exhaustive coverage.

### 1.1 Objectives
- Design 5–6 prioritized test scenarios from the feature specification, covering happy paths, negative/validation cases and boundary conditions.
- Prioritize scenarios by risk, focusing on functional requirements, business rules and validation.
- Run the top 3 scenarios and report high-impact defects with clear, reproducible evidence.
- Identify which scenarios to automate (one E2E UI test, one API test) and which stay manual, with reasons.


### 1.2 Scope

- **Platform:** Desktop web application, latest Chrome
- **Sport:** Football / soccer
- **Event type:** Upcoming / pre-match matches
- **Bet type:** Single bet, one active selection at a time
- **UI features:** Match list, outcome selection (1 / X / 2), bet slip, place-bet - interaction, success receipt, error modal, date and odds filters
- **API:** GET `/api/matches`, GET `/api/balance`, POST `/api/reset-balance`, POST `/api/place-bet`
- **Rules:** Business rules and validation rules

### 1.3 Out Of Scope
- Live / in-play betting
- Multi-bets and accumulators
- Sports other than football
- Mobile devices and mobile-specific UX
- Browsers other than Chrome (Firefox, Safari, Edge)
- Performance, load, and security / penetration testing
- Accessibility and localization, Visual Testing, Usability Testing
- CI/CD pipeline integration

### 1.4 System Overview
Single Bet Placement is the core betting flow: a customer picks an outcome (1 / X / 2) on an upcoming football match, enters a stake in the bet slip, and places the bet. The bet either succeeds, in which case the stake is deducted and a receipt popup is shown, or fails with a descriptive error. The UI uses an existing REST API, documented in Swagger, and every request identifies the user with the x-user-id header. Full details are in the [Feature Specification – Single Bet Placement](../../docs/Feature_Specification.pdf).


### 1.5 Definitions/Acronyms
For full feature details and domain terms, see the source documents:
- [Feature Specification – Single Bet Placement](../../docs/Feature_Specification.pdf)
- [HQA Take Home Task](../../docs/HQA_Take_Home_Task.pdf)

## 2. Approach

### 2.1 Assumptions
- Test scenario is treated as a test case
- Minimum stake is assumed to be **€1.00** per bet based on  business rules table, even though the validation table says €1.01
- Currency is **EUR (€)** in both the UI and the API.
- The starting balance is **€125.50**, the value POST `/api/reset-balance` restores it (see Swagger).
- max odds is 10.0 not 1000.00
- "Upcoming" means the kickoff date is today or later. Matches with an earlier date should not be bettable or displayed.
- Kickoff must show date and time, as the feature specification says, even if the API/Swagger returns only a date `YYYY-MM-DD`.
- Only latest desktop Chrome is supported.

### 2.2 Test Coverage
Coverage is measured against the feature specification and comes from two types of execution: scripted testing covers the **known requirements**, and exploratory testing finds the **unknown risks** that scripted cases miss. See [Test Execution Sessions](#35-test-execution-sessions).

- **Scripted testing:** test cases designed from the functional requirements and business rules, mapped to requirements in a traceability matrix. See [Scripted Testing](#351-scripted-testing).
- **Exploratory testing:** unscripted, time-boxed sessions guided by experience and error guessing. See [Exploratory Testing](#352-exploratory-testing).

### 2.3 Test Tools

| Purpose | Tool |
|---------|------|
| Automation framework | [sportsbet-test-framework](https://github.com/AlejandroAreiza/sporty-home-assignment/tree/main/sportsbet-test-framework) (Python, Screenplay pattern) |
| Reporting | Allure |
| Task runner | Makefile |
| Test management | Markdown files in this repository |

### 2.4 Test Type

| Type | Purpose | Execution |
|------|---------|-----------|
| **Exploratory** | Time-boxed, unscripted checks around the bet placement flow | Manual |
| **E2E UI and API** | Full user journey | Manual + Automated |
| **API** | Business and validation rules directly on the endpoints: status codes, response body, currency, balance | Automated |


**Note:** Unit and component tests belong to the development team and are outside this plan.


## 3. Test Execution

Test execution focuses on **quality, not quantity**: a few well-chosen, high-risk test cases that find the issues with the highest business impact.

### 3.1 Test Environment

| Item | Value |
|------|-------|
| Application (SUT) | https://qae-assignment-tau.vercel.app/ |
| User ID | `candidate-ZrzbrQMxczHo` |
| Swagger UI | https://qae-assignment-tau.vercel.app/api/docs |
| Auth header (API) | `x-user-id: candidate-ZrzbrQMxczHo` |
| Browser | Latest desktop Chrome |

### 3.2 Test Cases Attributes

| Attribute | Description |
|-----------|-------------|
| **ID & Title** | `TC-XX` plus a short summary of what is tested |
| **Priority** | Critical / High / Medium / Low (see below) |
| **Label** | Automated / Manual Only / Automation candidate (see below) |
| **Risk Rationale** | Use it to show you understand which risks drive your test selection |
| **Preconditions** | State the system must be in before the test starts |
| **Test Data** | Input values used in the test, based on the business rules |
| **Steps** | Numbered actions to run the test |
| **Expected Result** | The outcome the feature specification requires |


| Priority | Meaning  |
|----------|---------|
| **Critical** | Core money flow or bet integrity. Failure blocks release. Always executed.|
| **High** | Key business rule or validation with direct financial or user impact|
| **Medium** | Important but with a workaround or limited impact |
| **Low** | Cosmetic or rare edge cases |



| Label | Meaning |
|-------|---------|
| **Automated** | Implemented in the automation framework and runs from there |
| **Manual Only** | Run manually only. Too complex, too costly, or too unstable to automate for now. The reason is noted in the test case |
| **Automation candidate** | Run manually for now; a good fit for automation as the next step |

### 3.3 Bug Attributes
Every bug found during scripted or exploratory testing is logged in [bug-reports.md](../reports/bug-reports.md).


| Attribute | Description |
|-----------|-------------|
| **Bug ID & Title** | `BUG-XX` plus a short summary of the problem |
| **Severity** | Critical / High / Medium / Low (see below) |
| **Reproduction Steps** | Numbered, minimal steps including test data and user ID |
| **Expected vs Actual** | What the spec says vs what happened |
| **Business Impact** | One sentence on the consequence for the user or business |
| **Evidence** | Screenshot, API request/response, or a short note |


| Severity | Meaning |
|----------|---------|
| **Critical** | Money or bet integrity is broken, or the core flow is blocked. No workaround |
| **High** | A key rule or function fails, with a large impact or a poor workaround |
| **Medium** | Partial or non-core failure, with a reasonable workaround |
| **Low** | Cosmetic or minor issue, no functional impact |

### 3.4 Test Cases

| ID & Title | Priority | Label | Risk Rationale | Preconditions | Test Data | Steps | Expected Result |
|------------|----------|-------|----------------|---------------|-----------|-------|-----------------|
| **TC-01** Place a valid single bet on an upcoming match | Critical | Automated (E2E UI) | Core money flow. If the stake is not deducted, the payout is wrong, or the receipt doesn't match the bet slip, users lose money or trust. | 1. User is logged in (app opened with `?user-id=candidate-ZrzbrQMxczHo`).<br>2. Balance is reset (`POST /api/reset-balance`). | **Selection:** `1`, `X` or `2`.<br>**Stake:** any value from €1.00 to €100.00, up to 2 decimals (e.g. `10.00`). | 1. Note the balance in the header.<br>2. On an upcoming match, click the `selection` odds and note the odds.<br>3. Enter the `stake` in the bet slip.<br>4. Click `Place Bet button`.<br>5. Close the receipt. | 1. Balance is shown in the header.<br>2. Bet slip shows the match in the correct order (home vs away), selection, odds, and `Place Bet button` is disabled.<br>3. `Place Bet button` is enabled, total stake is shown, and potential payout = `stake × odds`.<br>4. Button shows `Placing...`, then a receipt with Bet ID, match (home vs away), selection, stake, odds, payout (`stake × odds`) and timestamp, all matching the bet slip.<br>5. No active selection; `balance = initial balance − stake` in the header and bet slip. |
| **TC-02** Enforce the maximum stake boundary via the API | High | Automated (API) | Stake limits protect users and the business from over-exposure. If only the UI enforces them, anyone can bypass the limit by calling the API directly. | 1. Balance is reset (`POST /api/reset-balance`).<br>2. A valid upcoming `matchId` is available from `GET /api/matches`. | **Technique:** Boundary Value Analysis on stake max (€100.00, step €0.01).<br>**Header:** `x-user-id: candidate-ZrzbrQMxczHo`.<br>**Body:** `{"matchId": "<valid id>", "selection": "HOME", "stake": <value>}`<br>• `100.01`: just above max → invalid<br>• `100.00`: on the max → valid | 1. Call `GET /api/matches` and take the `id` of an upcoming match.<br>2. Call `POST /api/place-bet` with stake `100.01`.<br>3. Call `GET /api/balance`.<br>4. Call `POST /api/place-bet` with stake `100.00`.<br>5. Call `GET /api/balance`. | 1. Status code `200` with the list of matches.<br>2. Status code `422` and response body `{"error": "invalid_stake_max","message": "Stake must be at most 100.00."}`.<br>3. Status code `200` with body `{"balance": {{reset-balance}}, "currency": "EUR"}`; balance unchanged.<br>4. Status code `200`; response has `stake: 100` and `payout = 100 × odds`.<br>5. Status code `200` with body `{"balance": {{reset-balance}}-{{stake}}, "currency": "EUR"}`. |
| **TC-03** Reject a bet when the stake exceeds the available balance | Critical | Automation candidate (UI + API) | Users must never bet money they don't have. If the backend doesn't check the balance, users build up debt and the business loses money. | 1. User is logged in.<br>2. Balance is reset (`POST /api/reset-balance`). | **Stake:** a value above the available balance, e.g. `100.00` when €20.00 is left. | 1. Place a bet with stake `100.00`.<br>2. Without refreshing, place another bet with stake `100.00`.<br>3. Call `GET /api/balance`. | 1. Bet is placed; balance = initial balance − €100.00.<br>2. Bet is rejected with **"Insufficient balance"** in the UI; the API returns status code `422`.<br>3. Status code `200`; balance is the same as after step 1 and never below €0.00. |
| **TC-04** Reject bets on past matches via the API | High | Automation candidate (API) | Betting on matches that have already been played lets users bet on known results, a direct financial and integrity risk. Testing it via the API proves the backend blocks it, even if the UI shows past matches. | 1. Balance is reset (`POST /api/reset-balance`).<br>2. `GET /api/matches` returns at least one match with `kickoffDate` before today. | **Header:** `x-user-id: candidate-ZrzbrQMxczHo`.<br>**Body:** `{"matchId": "<past match id>", "selection": "HOME", "stake": 10.00}`. | 1. Call `GET /api/matches` and take the `id` of a match with `kickoffDate` before today.<br>2. Call `POST /api/place-bet` with the test data body.<br>3. Call `GET /api/balance`. | 1. Status code `200` with the list of matches.<br>2. Status code `422`; the bet is not placed.<br>3. Status code `200`; balance is unchanged. |
| **TC-05** Double submit does not place duplicate bets | High | Manual Only | A double click must never charge the user twice. Manual Only: the result depends on click timing and network speed, so an automated check would be unreliable. | 1. User is logged in.<br>2. Balance is reset (`POST /api/reset-balance`). | **Selection:** `1`, `X` or `2`.<br>**Stake:** any value from €1.00 to €100.00 (e.g. `80.00`). | 1. Click the selection odds on an upcoming match.<br>2. Enter the stake in the bet slip.<br>3. Click `Place Bet` several times quickly while it shows `Placing...`.<br>4. Close the receipt and check the balance. | 1. Bet slip shows the selection.<br>2. `Place Bet` is enabled.<br>3. `Place Bet` is disabled while `Placing...`; only one bet is placed, and any extra request returns status code `409`.<br>4. `Balance = initial balance − stake`, deducted once. |

**Why TC-05 is Manual Only:** the bug only appears when a second click lands while the first bet is still `Placing...`. That window changes with network speed and server load, so an automated check would pass or fail at random (flaky). A tester can slow the network in DevTools, retry until the issue shows, and record evidence (screen recording and Network tab). The backend part (parallel requests → one `200`, the rest `409`) is a candidate for a future API test.

**Requirements Traceability Matrix**

| Requirement (spec) | TC-01 | TC-02 | TC-03 | TC-04 | TC-05 | Exploratory | Coverage |
|--------------------|:-----:|:-----:|:-----:|:-----:|:-----:|-------------|----------|
| §2.1 Match List (upcoming only, home vs away, 1/X/2 odds) | ✅ | | | ✅ | | Match count label | Covered |
| §2.2 Bet Slip (one selection, stake, balance, payout, remove) | ✅ | | | | | Change / single / remove selection | Covered |
| §2.3 Place Bet Interaction (`Placing...`, one outcome, stake deducted) | ✅ | | | | ✅ | Repeated bets | Covered |
| §2.4 Success Receipt | ✅ | | | | | - | Covered |
| §2.5 Error Modal (Rebet / Close) | | | | | | - | **Not covered**: a server error can't be triggered on demand |
| §2.6 Filters (date, odds) | | | | | | Date filter, odds filter | Exploratory only |
| §3 Business Rules: stake min / precision | | | | | | Stake input validation | Exploratory only |
| §3 Business Rules: stake max | | ✅ | | | | Stake input validation | Covered |
| §3 Business Rules: upcoming matches only | | | | ✅ | | - | Covered |
| §3 Business Rules: currency EUR | | ✅ | | | | - | Covered |
| §4.1 Stake Validation (UI + API) | | ✅ | ✅ | | | Stake input validation | Covered |
| §4.2 Selection and Match Validation | | | | ✅ | | - | Partly (match only) |
| §4.3 Request / Protocol Validation | | | | | | - | **Not covered**: lower risk |
| §4.4 UI Error Messaging | | | ✅ | | | Stake input validation | Covered |
| §5.3 `POST /api/place-bet` | | ✅ | ✅ | ✅ | ✅ | Repeated bets | Covered |
| §5.3 `POST /api/reset-balance` | | | | | | Balance reset | Exploratory only |

**Note:** For automation, follow the setup in the [sportsbet-test-framework README](../../sportsbet-test-framework/README.md).

### 3.5 Test Execution Sessions

#### 3.5.1 Scripted Testing
  1. Run the top 3 priority test cases from [Test Cases](#34-test-cases).
  2. Mark each test case as Pass or Fail:
     - **Pass:** every step gives the expected result.
     - **Fail:** any expected result is not met.
  3. Log bugs in [bug-reports.md](../reports/bug-reports.md).
  4. Record results in [test-execution-report.md](../reports/test-execution-report.md): each test case with its status and the bugs it found (e.g. `TC-01 → BUG-02`).

**Hard vs soft assertions:**
- **Hard assert:** stops the test at the first failure.
- **Soft assert:** records the failure and continues; the test fails at the end with all failures listed.

#### 3.5.2 Exploratory Testing
1. Run short, time-boxed sessions (15–30 min) around the bet placement flow.
2. Focus on what scripted cases miss: timing, retries, unusual input, and UI/API consistency.
3. Record session notes in the exploratory section of [test-execution-report.md](../reports/test-execution-report.md).
4. Log bugs in [bug-reports.md](../reports/bug-reports.md)