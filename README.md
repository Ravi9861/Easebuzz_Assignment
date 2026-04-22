# Easebuzz_Assignment
**Task 5: Strategy & Leadership**

**1. Handling Flaky Tests & Sprint Velocity Drop**

Flaky tests directly impact team confidence and sprint velocity, so my approach focuses on **stabilization + process improvement**.

Step 1: Identify & Measure
- Analyze failure trends using CI reports
- Track flaky tests separately (failure vs rerun pass)
- Create a **Flaky Test Dashboard**

Step 2: Root Cause Categorization
- Synchronization issues (timing/waits)
- Environment instability
- Test data dependency
- Third-party/API failures

Step 3: Stabilization Strategy
- Replace hard waits with **explicit/auto waits (Playwright)**
- Use **API mocking/stubbing** for unstable services
- Implement **retry mechanism (pytest-rerunfailures)**
- Use **isolated and deterministic test data**
- Parallel execution with proper test isolation

Step 4: Team Ownership
- Assign a **Flaky Test Owner (rotation basis)**
- Set SLA: fix flaky tests within 1–2 sprints
- Code review checklist for automation stability

Step 5: CI/CD Optimization
- Separate pipelines:
  - Stable suite (blocking release)
  - Flaky suite (non-blocking, monitored)
- Run nightly full regression

Outcome
- Improved pipeline stability by ~30–40%
- Faster sprint velocity and reduced false failures

---

**2. Critical Bugs Missed in Production**

Handling production defects requires **immediate action + long-term prevention**.

Step 1: Immediate Response
- Reproduce issue quickly
- Collaborate with dev team for **hotfix**
- Validate fix in staging before release

Step 2: Root Cause Analysis (RCA)
- Was it:
  - Missing test coverage?
  - Requirement gap?
  - Environment mismatch?
  - Data-related issue?

Step 3: Strengthen Test Coverage
- Add:
  - Edge cases & boundary conditions
  - Negative scenarios
  - API + UI integration tests
- Introduce **contract/schema validation for APIs**

Step 4: Process Improvement
- Improve requirement grooming with QA involvement
- Introduce **test design reviews before sprint execution**
- Add **pre-release QA checklist**
- Increase automation coverage for critical flows

Step 5: Team & Culture
- Promote **blameless culture**
- Conduct knowledge-sharing sessions
- Document learnings to avoid repeat issues

Outcome
- Reduced production defects significantly
- Improved release confidence and product quality
