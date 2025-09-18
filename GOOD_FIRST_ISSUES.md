# Good First Issues (8)

Pick one, open a PR, and keep the change small.

---

## 1) Calculator: add modulo `%`

- Area: `calculator_cli`
- Done when:
  - `%` works in the REPL and help text
  - README shows an example
  - `% 0` gives a clear error

## 2) Todo CLI: `edit <id> <new title>`

- Area: `todo_cli`
- Done when:
  - `edit` updates a todo title
  - README shows usage

## 3) Stopwatch: export laps to CSV

- Area: `stopwatch_cli`
- Done when:
  - `lap export` writes `laps.csv`
  - README mentions it

## 4) File Organizer: `--dry-run-summary`

- Area: `file_organizer`
- Done when:
  - Summary prints category -> count after dry-run
  - README mentions the flag

## 5) Quiz Game: shuffle and optional `--timer`

- Area: `quiz_game`
- Done when:
  - Questions are shuffled by default
  - Optional `--timer` documented

## 6) Docs: add 3 screenshots/GIFs

- Area: docs/assets
- Done when:
  - Add demos for `guess_number`, `calculator_cli`, `todo_cli`
  - Link them in READMEs

## 7) Tests: calculator error paths

- Area: tests
- Done when:
  - Add tests for invalid tokens, unsupported operator, divide by zero
  - Tests pass locally

## 8) DSA tests: arrays

- Area: `dsa/tests`
- Done when:
  - Add cases for `two_sum` (negatives, no-solution) and `max_subarray` (single element)
