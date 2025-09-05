<!-- Common documentation sections that can be included in multiple files -->

## Prerequisites

- Python 3.8+ installed
- Windows PowerShell or a Unix shell (macOS/Linux)

## How to Run (From Repository Root)

- Windows PowerShell: `python .\level1\<project_folder>\main.py`
- macOS/Linux: `python3 ./level1/<project_folder>/main.py`

## Demo Section Template

Placeholder for screenshot or GIF. Add your file under `docs/assets/` and link it here.

Example:
```markdown
![Demo](../docs/assets/project-screenshot.gif)
```

## Common Project Structure

```
project/
├── main.py          # Main application file
├── README.md        # Project documentation
└── [data files]     # Optional data files (CSV, JSON, etc.)
```

## Testing

Run tests with pytest:
```bash
python -m pytest
```

## Contributing

- Follow the style guidelines in `CONTRIBUTING.md`
- Add type hints for public functions
- Include docstrings for complex functions
- Test your changes before submitting
