# File Organizer

Organize files from a source directory into categorized folders under a destination directory. Supports a JSON config and dry-run.

## How to Run

- **Prerequisites**: Python 3.8+
- **Run**:
  - Windows PowerShell:
    - `python .\main.py organize <src> <dest> [--config path] [--dry-run]`
  - macOS/Linux:
    - `python3 ./main.py organize <src> <dest> [--config path] [--dry-run]`

## Config

Config JSON maps category names to a list of extensions:

```json
{
  "images": [".png", ".jpg"],
  "documents": [".pdf", ".txt"]
}
```

## Examples

```
python .\main.py organize C:\Downloads C:\Sorted --dry-run
python .\main.py organize C:\Downloads C:\Sorted --config rules.json
```

## Demo

Placeholder for screenshot or GIF. Add your file under `docs/assets/` and link it here.


