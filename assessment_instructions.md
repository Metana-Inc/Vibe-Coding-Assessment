# Assessment Instructions

**Duration:** 2.5–3 hours  
**Tools Allowed:** Any AI coding assistant (Cursor, Copilot, Claude, etc.)

---

## Part 1: Git & GitHub Fundamentals

**Time Allocation:** 30–40 minutes

### Task 1.1: Repository Setup

1. Fork this repository: [https://github.com/Metana-Inc/Vibe-Coding-Assessment](https://github.com/Metana-Inc/Vibe-Coding-Assessment) to your GitHub account.
2. Clone your fork locally.
3. Create a new branch named: `feature/add-tasks-api`

### Task 1.2: First Commit

1. Add your name and the current date as a comment in `app/main.py`.
2. Commit the change using a clear and meaningful commit message.

### Task 1.3: Merge Conflict Resolution

The assessor will push a change to the repository. You are required to:

- Fetch the latest changes.
- Merge or rebase your branch.
- Resolve any merge conflicts correctly.
- Push the resolved changes to your branch.

---

## Part 2: AI-Assisted Feature Development

**Time Allocation:** 45–60 minutes

### Task 2.1: POST /tasks Endpoint

Implement a POST endpoint to create a new task.

**Request Requirements:**

Fields:
- `title` (string, required)
- `user_email` (string, required, must exist in the system)
- `priority` (string, required, allowed values: `low`, `medium`, `high`, `critical`)

Behavior:
- A unique `task_id` must be auto-generated.
- Default status is `pending`.
- Input must be validated; invalid input must return appropriate errors.

**Expected Responses:**

| Code | Description |
|------|-------------|
| `201 Created` | Task successfully created; return full task object including generated `task_id`, status, timestamps. |
| `400 Bad Request` | Input validation fails (e.g., missing fields, invalid priority). |
| `404 Not Found` | `user_email` does not exist in the system. |

---

### Task 2.2: GET /tasks Endpoint

Implement a GET endpoint to retrieve tasks with filtering, sorting, and optional pagination.

**Filtering Parameters (optional):**
- `user_email` — Return tasks assigned to a specific user
- `status` — Filter by task status
- `priority` — Filter by task priority

**Sorting Options (optional):**
- `priority_score` — Descending by priority importance
- `due_date` — Ascending
- `created_at` — Descending

**Behavior:**
- If no filters are provided, return all tasks with default sorting by `created_at` descending.
- Support multiple filters at once.
- Paginate results with `limit` and `offset` query parameters.

---

### Task 2.3: Security Review

Document findings in `REVIEW_NOTES.md` by answering:

- What happens if `priority` is provided in uppercase?
- What happens if the `title` is extremely long (e.g., 10,000 characters)?
- Is user input properly sanitized to prevent injection or other vulnerabilities?

---

## Part 3: Debugging When AI Fails

**Time Allocation:** 45–60 minutes

### Task 3.1: Run the Test Suite

Run the following command:

```bash
pytest tests/test_utils.py -v
```

> **Note:** Multiple tests are expected to fail. This is intentional.

---

### Task 3.2: Bug Documentation

For each failing test, document the following in `BUG_REPORT.md`:

- Name of the failing test
- Expected behavior versus actual behavior
- Root cause analysis
- Description of the fix applied

---

### Task 3.3: Bug Fixes

Fix the issues described below:

| Bug # | Function |
|-------|----------|
| 1 | `validate_email()` |
| 2 | `calculate_priority_score()` |
| 3 | `sanitize_input()` |
| 4 | `parse_date()` |

---

## Part 4: Submission

**Time Allocation:** 15 minutes

1. Ensure all tests pass successfully.
2. Open a Pull Request that includes:
   - A summary of the implementation
   - A list of bugs fixed
   - The AI tool(s) used
   - A reflection on where AI was helpful and where it failed

---

## Grading Rubric

| Category | Points |
|----------|--------|
| Git Usage | 20 |
| Feature Implementation | 25 |
| Code Quality | 15 |
| Bug Fixes | 25 |
| Documentation | 10 |
| Reflection | 5 |
| **Total** | **100** |

**Passing Score: 70 points**
