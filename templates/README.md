# Templates

This directory contains templates for generating consistent project documentation and code.

## Project README Template

Use `templates/project_readme_template.md` to generate consistent READMEs for all projects.

### Usage

```bash
# Generate a README for a project
python scripts/generate_readme.py <project_path> templates/project_readme_template.md
```

### Template Variables

- `{{PROJECT_NAME}}` - Auto-generated from project directory name
- `{{PROJECT_TYPE}}` - Auto-detected (CLI, Game, Tool)
- `{{PROJECT_DESCRIPTION}}` - Basic description with level info
- `{{USAGE_SECTION}}` - Placeholder for project-specific usage
- `{{NOTES_SECTION}}` - Placeholder for additional notes

### Example

```bash
# Generate README for guess_number project
python scripts/generate_readme.py basic_programs/guess_number templates/project_readme_template.md
```

## Adding New Templates

1. Create your template file in this directory
2. Use `{{VARIABLE_NAME}}` for placeholders
3. Update the generation script if needed
4. Document usage in this README

## Template Best Practices

- Use descriptive variable names
- Include comments for complex sections
- Keep templates focused on structure, not content
- Test templates with real projects before committing
