#!/usr/bin/env python3
"""
Script to generate project READMEs from templates.
Usage: python scripts/generate_readme.py <project_path> <template_path>
"""

import sys
from pathlib import Path
from typing import Dict


def load_template(template_path: str) -> str:
    """Load template file content."""
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()


def generate_readme(template: str, replacements: Dict[str, str]) -> str:
    """Replace placeholders in template with actual values."""
    result = template
    for key, value in replacements.items():
        result = result.replace(f"{{{{{key}}}}}".upper(), value)
    return result


def main():
    if len(sys.argv) != 3:
        print("Usage: python scripts/generate_readme.py <project_path> <template_path>")
        sys.exit(1)

    project_path = Path(sys.argv[1])
    template_path = Path(sys.argv[2])

    if not template_path.exists():
        print(f"Template not found: {template_path}")
        sys.exit(1)

    # Extract project info from path
    project_name = project_path.name
    level = project_path.parent.name
    project_type = "CLI" if "cli" in project_name else "Game" if "game" in project_name else "Tool"

    # Load template
    template = load_template(template_path)

    # Define replacements (these could be made configurable)
    replacements = {
        "PROJECT_NAME": project_name.replace("_", " ").title(),
        "PROJECT_TYPE": project_type,
        "PROJECT_DESCRIPTION": f"A {project_type.lower()} project in {level}.",
        "USAGE_SECTION": "## Usage\n\nDescribe how to use this project.",
        "NOTES_SECTION": "## Notes\n\nAny additional notes about the project."
    }

    # Generate README content
    readme_content = generate_readme(template, replacements)

    # Write to project README
    readme_path = project_path / "README.md"
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print(f"Generated README for {project_name} at {readme_path}")


if __name__ == "__main__":
    main()
