#!/usr/bin/env python3
"""
Script to include common sections in documentation files.
Usage: python scripts/include_sections.py <target_file> <section_name>
"""

import sys
from pathlib import Path
import re


def load_common_sections() -> dict:
    """Load common sections from docs/common_sections.md"""
    sections_file = Path("docs/common_sections.md")
    if not sections_file.exists():
        print("Error: docs/common_sections.md not found")
        sys.exit(1)

    with open(sections_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse sections (assuming ## headers)
    sections = {}
    current_section = None
    current_content = []

    for line in content.split('\n'):
        if line.startswith('## '):
            # Save previous section
            if current_section:
                sections[current_section] = '\n'.join(current_content).strip()

            # Start new section
            current_section = line[3:].strip()
            current_content = []
        elif current_section:
            current_content.append(line)

    # Save last section
    if current_section:
        sections[current_section] = '\n'.join(current_content).strip()

    return sections


def include_section(target_file: Path, section_name: str, sections: dict) -> None:
    """Include a common section in the target file"""
    if section_name not in sections:
        print(f"Error: Section '{section_name}' not found in common sections")
        return

    # Read target file
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Look for include comment
    include_pattern = rf'<!-- INCLUDE: {re.escape(section_name)} -->'
    replacement = f'<!-- INCLUDE: {section_name} -->\n\n{sections[section_name]}\n\n<!-- END INCLUDE: {section_name} -->'

    if re.search(include_pattern, content):
        new_content = re.sub(include_pattern, replacement, content)

        # Write back
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"Included section '{section_name}' in {target_file}")
    else:
        print(f"Include marker for '{section_name}' not found in {target_file}")


def main():
    if len(sys.argv) != 3:
        print("Usage: python scripts/include_sections.py <target_file> <section_name>")
        print("Available sections:")
        sections = load_common_sections()
        for section in sections:
            print(f"  - {section}")
        sys.exit(1)

    target_file = Path(sys.argv[1])
    section_name = sys.argv[2]

    if not target_file.exists():
        print(f"Error: Target file {target_file} not found")
        sys.exit(1)

    sections = load_common_sections()
    include_section(target_file, section_name, sections)


if __name__ == "__main__":
    main()
