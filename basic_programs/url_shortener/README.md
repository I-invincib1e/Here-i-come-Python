# URL Shortener

Create short codes for long URLs and expand them later.

## How It Works

- Generates a short code from the MD5 hash of the URL (first N chars)
- Ensures uniqueness; on collision, uses a longer prefix
- Keeps two maps in memory: `code->url` and `url->code`
- Persists mappings to a simple `urls.txt` (comma-separated)

## Example

```text
Enter long URL: https://example.com/very/long
Short URL: a1b2c3
Enter short code: a1b2c3
Original URL: https://example.com/very/long
```

## Internals

- `shorten_url(long_url)` builds and stores the short code
- `expand_url(code)` returns the original URL or a message
- `save_to_file` / `load_from_file` manage persistence

## Note

Local demo only; real services use HTTP endpoints and a database.
