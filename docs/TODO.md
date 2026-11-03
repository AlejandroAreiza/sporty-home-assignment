# Sporty Task Challenge

## Progress

- [x] Understand the feature
- [x] Create repo
- [x] Test planning
  - [x] Define test design technique
  - [x] Create test plan document
  - [x] Refine test plan
- [x] Test execution
  - [x] Create test execution report md file
  - [x] Perform test execution based on test plan
  - [x] Perform exploratory testing
- [x] Bugs
  - [x] Create bug report md file
  - [x] Report bugs
- [ ] Automation
  - [x] Build target automation framework
  - [ ] Automate E2E test
  - [x] Automate API test
  - [ ] Execute tests
- [ ] Strategy & recommendations
  - [ ] Write strategy-and-recommendations.md

---

## General Deliverable Requirements

### Submission
- All deliverable files must be included in a **public GitHub repository**.
- A focused submission with clear rationale scores higher than a large one with weak justification.

### Repository Structure

```
sporty-home-assignment/
├── README.md
├── manual-qa-test-strategy/
│   ├── test-plan/
│   │   └── test-plan-single-bet-placement.md
│   └── reports/
│       ├── test-execution-report.md
│       └── bug-reports.md
├── sportsbet-test-framework/
│   ├── README.md
│   ├── requirements.txt
│   ├── screenplay/
│   │   ├── core.py
│   │   ├── abilities.py
│   │   ├── interactions.py
│   │   ├── tasks.py
│   │   └── questions.py
│   └── tests/
│       ├── conftest.py
│       ├── test_place_single_bet.py
│       └── test_bet_validation.py
└── strategy-and-recommendations/
    └── strategy-and-recommendations.md
```

### Deliverables Checklist

| Part | Deliverable | File |
|------|-------------|------|
| A1 | Test plan | `manual-qa-test-strategy/test-plan/test-plan-single-bet-placement.md` |
| A2 | Test execution results | `manual-qa-test-strategy/reports/test-execution-report.md` |
| A2 | Bug reports | `manual-qa-test-strategy/reports/bug-reports.md` |
| B3 | Automation framework + README | `sportsbet-test-framework/` |
| C | Strategy & recommendations | `strategy-and-recommendations/strategy-and-recommendations.md` |

> **Note:** The assignment brief names the A2 files `execution-results.md` and `bugs.md`. Decide which names to use and keep them consistent.

### Assumptions
- "Test scenario" is treated as a test case.

---

## Part A — Manual QA & Test Strategy

### A1. Test Plan

**Goal:** Review the Single Bet Placement Feature Specification and design a test plan with 5–6 prioritized test scenarios.

**Test plan must include**
- Traceability matrix (maps requirements against test cases)
- Risks and mitigation plan
  - e.g. a high-priority test case that can't be automated due to complexity, so it's agreed to run it manually under defined conditions
- Candidates for automation

**Scenario coverage**
- 5–6 prioritized test scenarios
- The set should show range across:
  - Happy paths
  - Negative / validation cases
  - Boundary conditions (boundary value analysis)

**Scenario attributes**

| Attribute | Values / Notes |
|-----------|----------------|
| Id | — |
| Title | — |
| Labels | Manual Only, Automated |
| Priority | Critical, High, Medium, Low |
| Risk rationale | Show which risks drive the test selection (risk-based testing) |
| Steps | — |
| Expected Result | — |

**Approach** — strategic thinking and clean engineering over exhaustive coverage:
- Risk-based testing
- Traceability matrix
- Testing type techniques
- Test case design techniques

### A2. Test Execution

**Tasks**
- Pick the top 3 of the 5–6 scenarios from the test plan and run them against the application.
- Spend a few minutes on quick exploratory testing around the bet placement flow.
- Report execution results and bugs in separate md files.

**Defect attributes** — document each defect found during execution or exploration:

| Attribute | Values / Notes |
|-----------|----------------|
| Id | — |
| Title | — |
| Severity | Critical, High, Medium, Low |
| Reproduction Steps | — |
| Expected vs Actual Result | — |
| Business Impact | One sentence on the user/business consequence |
| Evidence | Screenshot or brief note |

**Scoring**
- Scored on report quality, not bug count.
- Quality over quantity — focus on high-impact issues.

---

## Part B — Automation

### B3. Framework and Automated Tests

**Tasks**
- Build a small, well-structured automation project using the tech stack below.
- Implement 2 high-value automated tests from the test plan:
  - **E2E UI test:** a critical user journey
  - **API test:** a validation or business rule check via the API directly
  - Each test has a brief comment or docstring explaining why it was chosen.
- Write a README with clear setup and run instructions (include Mermaid diagrams).

**Tech stack**
- Python
- Selenium + pytest
- `requests` library
- Latest desktop Chrome
- Poetry or uv for dependency management
- Allure for reporting (or evaluate an alternative)
- Docker for Selenium / Selenium Grid
- Makefile

**Code rules**
- Clean, small but well-structured project
- Readable, maintainable code following Python conventions
- Design principles: SOLID, KISS, YAGNI, etc.
- Scalable automation design pattern: **Screenplay**

**Scope**

| In scope | Out of scope |
|----------|--------------|
| Test app: https://qae-assignment-tau.vercel.app/ | CI/CD |
| Chrome | Firefox, Safari |
| | Parallel execution |
| | Data-driven testing from external files (inline `pytest.mark.parametrize` is used for boundary values) |

---

## Part C — Strategy & Recommendations

Write a short document (`strategy-and-recommendations.md`) covering:
- Why these 2 tests were selected for automation over other candidates
- What was intentionally left manual-only and why
- Top 2–3 recommendations if the project were to scale (CI/CD, additional test layers, data strategy, spec clarifications, etc.)

**Recommendation ideas**
- [ ] Test data management: move test data (e.g. stake boundaries) to JSON/YAML files loaded by a fixture, so new cases need no code change
- [ ] BUG-06 is data-dependent (payout truncation only shows for some odds, e.g. 4.1): add a regression test with fixed test data (a known 4.1-odds match) to make it deterministic
- [ ] make files
- [ ] video in allure report
---

# Feature Specification: Single Bet Placement

**User ID:** `candidate-ZrzbrQMxczHo`

## 1. Feature Overview
Users can place a single bet on a sport event outcome.

| In scope | Out of scope |
|----------|--------------|
| Web application | Mobile |
| Football (soccer) | Other sports |
| Pre-match / upcoming only (no bets once the game has started) | Live betting |
| Single bet only (one selection per bet, no accumulators) | Multi bets |

## 2. Functional Requirements

### 2.1 Match List
**Observations**
- The platform displays past matches in the UI.
- Odds are enabled on past matches in the UI.
- No error on the API side.
- Kickoff date/time: API does not return time.
- Kickoff date/time: UI does not show time.

### 2.2 Bet Slip

### 2.3 Place Bet Interaction
**Observations**
- ⚠️ **High importance:** stake is not deducted on success, so the user can place bets indefinitely until the balance refreshes.

### 2.4 Success Receipt
**Observations**
- Potential payout is incorrect.

### 2.5 Error Modal

### 2.6 Filters
**Observations**
- Odds filter not working.

## 3. Business Rules

Useful for verification rules and test data.

| Rule                | Expected Behavior       |
|---------------------|-------------------------|
| Sport               | Football/Soccer only    |
| Event type          | Upcoming matches only   |
| Bet type            | Single bet only         |
| Stake min (per bet) | €1.00                   |
| Stake max (per bet) | €100.00                 |
| Stake precision     | Up to 2 decimal places  |
| Minimum odds        | 1.01                    |
| Maximum odds        | 1000.00                 |
| Odds behavior       | Static for session      |
| Currency            | EUR (€)                 |

**Observations**
- API returns the wrong currency (`USD` instead of `EUR`). Sample response:

```json
{
  "message": "Bet placed successfully",
  "matchId": "premier-league-newcastle-brighton-2026-09-02",
  "selection": "HOME",
  "stake": 1,
  "odds": 2,
  "payout": 2,
  "balance": 119,
  "currency": "USD"
}
```

## 4. Validation Rules
Guide for creating validation-based test cases.

### 4.1 Stake Validation (UI and API)
### 4.2 Selection and Match Validation
### 4.3 Request Protocol Validation
### 4.4 UI Error Messaging

## 5. Backend API
### 5.1 Authentication
### 5.2 API Documentation
### 5.3 Endpoints

## error guessing 

- double-clicking `Place Bet` or retrying during `Placing...` (double charge, `409`)
- stake values such as `0`, `-1`, `1.005`, `1,50`, `e`, spaces, very large numbers
- balance and payout rounding with odds that have 2+ decimals
- betting on past matches
- stale balance after a bet, or after a refresh
- currency or values in the API response that differ from the UI
- odds filter with min > max or empty values


## techa se techniques 
**Test design techniques used**
- **Boundary Value Analysis:** stake min/max (€0.99 / €1.00 / €100.00 / €100.01), precision (2 vs 3 decimals), stake vs balance.
- **Equivalence Partitioning:** valid / invalid stake classes (numeric, non-numeric, negative, empty) and selections (`HOME`, `DRAW`, `AWAY`, invalid).
- **State transition:** bet slip states (empty → selected → placing → success / error → empty).

| Data | Values |
|------|--------|
| Valid stakes | `1.00`, `10`, `25.50`, `100.00` |
| Boundary stakes | `0.99`, `1.00`, `1.01`, `99.99`, `100.00`, `100.01` |
| Invalid stakes | empty, `0`, `-5`, `abc`, `1.005`, `1,50` |
| Balance-related | a stake above the current balance (e.g. after reducing the balance) |
| Selections | `HOME`, `DRAW`, `AWAY`, plus invalid values via the API (`home`, `WIN`, empty) |
| Match IDs | a valid ID from the catalog, empty, unknown, and a past match |
| User context | valid `x-user-id`, missing header, empty header |

**Data reset:** before each test or session, call `POST /api/reset-balance` so the balance starts at €125.50 and results don't depend on earlier runs.


**Note:** hard asserts guard the flow, soft asserts check the details.
