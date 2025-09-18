# Todo CLI (JSON persistence)

A minimal todo manager that stores tasks in `todos.json` next to the script.

## How It Works

- Data model: `{ id, title, done }` stored in a JSON array
- `add <title>`: appends a new item with an auto-incremented `id`
- `list`: prints all todos with `[ ]` / `[x]` status
- `done <id>`: sets `done = True` for the matching item
- `del <id>`: removes the item by `id`
- Fault tolerance: invalid JSON or missing file yields an empty list

## Example

```text
> add Buy milk
Added.
> list
  1 [ ] Buy milk
> done 1
Completed.
> list
  1 [x] Buy milk
```

## Internals

- JSON read/write via `json` and `dataclasses.asdict`
- Next id computed from current max id in the list
