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
- [test case](#test-case)

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
| **Label** | Automated / Manual Only (see below) |
| **Requirement** | Spec section(s) covered (feeds the traceability matrix) |
| **Risk Rationale** | Use it to show you understand which risks drive your test selection |
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

| ID & Title | Priority | Label | Requirement | Risk Rationale | Steps | Expected Result |
|------------|----------|-------|-------------|----------------|-------|-----------------|
| **TC-01** Place a valid single bet on an upcoming match | Critical | Automated (E2E UI) | §2.1, §2.2, §2.3, §2.4, §3 | Core money flow. If the stake is not deducted, the payout is wrong, or the receipt doesn't match the bet slip, users lose money or trust. | 1. Reset balance (`POST /api/reset-balance`) and open the app with `?user-id=candidate-ZrzbrQMxczHo`.<br>2. Click the `1` odds on the first upcoming match and note the odds.<br>3. Enter stake `10.00` in the bet slip.<br>4. Click `Place Bet`.<br>5. Close the receipt. | 1. Header balance shows €125.50.<br>2. Bet slip shows the match in the correct order (home vs away), selection, odds and Place bet button is disabled.<br>3.Place bet button is enabled, total stake is `10.00` and Potential payout = `10.00 × odds`.<br>4. Button shows `Placing...`, then a receipt with Bet ID, match, selection, stake, odds, payout and timestamp, all matching the bet slip.<br>5. No active selection; balance is €115.50 in the header and bet slip. |

**Note:** For automation, follow the setup in the [sportsbet-test-framework README](../../sportsbet-test-framework/README.md).

### 3.5 Test Execution Sessions

#### 3.5.1 Scripted Testing
  1. Run the top 3 priority test cases from [Test Cases](#34-test-cases).
  2. Mark each test case as Pass or Fail:
     - **Pass:** every step gives the expected result.
     - **Fail:** any expected result is not met.
  3. Log bugs in [bug-reports.md](../reports/bug-reports.md).
  4. Record results in [test-execution-report.md](../reports/test-execution-report.md): each test case with its status and the bugs it found (e.g. `TC-01 → BUG-01`).

**Hard vs soft assertions:**
- **Hard assert:** stops the test at the first failure.
- **Soft assert:** records the failure and continues; the test fails at the end with all failures listed.

#### 3.5.2 Exploratory Testing
1. Run short, time-boxed sessions (15–30 min) around the bet placement flow.
2. Focus on what scripted cases miss: timing, retries, unusual input, and UI/API consistency.
3. Record session notes in the exploratory section of [test-execution-report.md](../reports/test-execution-report.md).
4. Log bugs in [bug-reports.md](../reports/bug-reports.md)


# test case
- login
- put all balance to user API
- choose a outcome
  - outcome button was selected
- put stake to the maximum
- verify bet slip details
- click on placement
- verify succeed bet placement
- verify updated balance
  - ui layer
  - api layer

