# File Organizer

Organize files from a source directory into categorized folders under a destination directory. Supports a JSON config and dry-run.

## How It Works

- Load rules: category → extensions (default or from a JSON config)
- Scan source directory and categorize by file extension
- Plan moves into target folders under destination
- With `--dry-run`, only prints planned moves; otherwise executes them

## Config Format

Config JSON maps category names to extension lists:

```json
{
  "images": [".png", ".jpg"],
  "documents": [".pdf", ".txt"]
}
```

## Example

```text
Would move:
  C:\Downloads\photo.png  ->  C:\Sorted\images\photo.png
  C:\Downloads\notes.txt  ->  C:\Sorted\documents\notes.txt
```

## Internals

- `categorize(file, rules)` returns a category by extension
- Simple planning and execution with `shutil.move`
