# Markdown Notes

Create, list, view, and render simple Markdown notes to HTML.

## How It Works

- Notes live in a local `notes/` folder next to the script
- `new <title> <content...>`: creates a safe filename and writes a `.md`
- `list`: shows available markdown files
- `view <file.md>`: prints markdown content
- `render <file.md>`: outputs basic HTML (headings, bold, italics)

## Example

```text
> new Shopping List Milk Eggs Bread
Created shopping_list.md
> list
shopping_list.md
> render shopping_list.md
<h1>Shopping List</h1>
...
```

## Internals

- Filenames sanitized via regex to avoid unsafe characters
- Simple markdown parsing for a subset of syntax
