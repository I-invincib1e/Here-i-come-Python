# Draft: Good First Issues (8)

Copy each to a new GitHub Issue. Suggested labels: `good first issue`, `help wanted`, `docs` or `tests`.

---

## 1) Calculator: Add modulo operator `%`
- Labels: good first issue, enhancement
- Area: `calculator_cli`
- Summary: Support `%` in the REPL and update README examples.
- Acceptance:
  - `%` handled in code and help text
  - README updated
  - Graceful error on `% 0`

## 2) Todo CLI: Add `edit <id> <new title>`
- Labels: good first issue, enhancement
- Area: `todo_cli`
- Summary: Implement an `edit` command to rename an existing todo by id.
- Acceptance:
  - `edit` updates the title
  - Usage shown in README examples

## 3) Stopwatch: Export laps to CSV
- Labels: good first issue, enhancement
- Area: `stopwatch_cli`
- Summary: Add `lap export` to save laps to a `laps.csv` next to the script.
- Acceptance:
  - Creates/overwrites `laps.csv`
  - README documents the feature

## 4) File Organizer: `--dry-run-summary`
- Labels: good first issue, enhancement
- Area: `file_organizer`
- Summary: Add a flag to print counts per destination folder after dry-run.
- Acceptance:
  - Summary printed with category -> count
  - README mentions the flag

## 5) Quiz Game: Shuffle questions and optional timer
- Labels: good first issue, enhancement
- Area: `quiz_game`
- Summary: Randomize questions each run; optional `--timer` per question.
- Acceptance:
  - Shuffle when no flags passed
  - Optional timer documented in README

## 6) Docs: Add screenshots/GIFs for 3 projects
- Labels: good first issue, docs
- Area: docs/assets
- Summary: Capture and add demo screenshots/GIFs for: `guess_number`, `calculator_cli`, `todo_cli`.
- Acceptance:
  - Files placed under `docs/assets/`
  - Linked in project READMEs Demo section

## 7) Tests: Add calculator error-path tests
- Labels: good first issue, tests
- Area: tests
- Summary: Add tests covering invalid tokens, unsupported operator, division by zero.
- Acceptance:
  - Tests pass locally
  - Clear names and assertions

## 8) DSA: Add more cases for arrays tests
- Labels: good first issue, tests
- Area: `dsa/tests`
- Summary: Extend tests for `two_sum` (negatives, no-solution) and `max_subarray` (single element).
- Acceptance:
  - New tests added and passing
