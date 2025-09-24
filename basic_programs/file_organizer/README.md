# File Organizer (Directory Management)

Organize files from a source directory into categorized folders based on file extensions. Supports custom JSON configuration and dry-run mode.

## How It Works

- Loads categorization rules from default settings or JSON config file
- Scans source directory recursively for all files
- Categorizes files by extension using predefined rules
- Creates organized folder structure in destination directory
- Supports dry-run mode to preview changes before execution

## Config Format

JSON configuration maps category names to file extension lists:

```json
{
  "images": [".png", ".jpg", ".jpeg", ".gif"],
  "documents": [".pdf", ".doc", ".txt", ".md"],
  "videos": [".mp4", ".avi", ".mkv"],
  "music": [".mp3", ".wav", ".flac"]
}
```

## Example

```text
Planning file organization...
Would move:
  C:\Downloads\photo.png  ->  C:\Sorted\images\photo.png
  C:\Downloads\report.pdf ->  C:\Sorted\documents\report.pdf
  C:\Downloads\song.mp3   ->  C:\Sorted\music\song.mp3

Use --dry-run to preview only, or run without flag to execute moves.
```

## Industry Applications

**Where file organization patterns are used in the real world:**

- **Content Management Systems**: WordPress, Drupal organize media files by type
- **Digital Asset Management**: Adobe Experience Manager, Bynder categorize creative assets
- **Data Pipeline Tools**: Apache Airflow, Prefect organize output files by processing stage
- **Backup Solutions**: Acronis, Veeam organize backup files by date/type hierarchies

**Learning Connection:** This demonstrates the foundation of file management systems used in media libraries, data warehouses, and automated content processing pipelines.

## Internals

- `categorize_file()`: Maps file extensions to category names using rule dictionary
- `scan_directory()`: Recursively finds all files in source directory
- `plan_moves()`: Creates move operations without executing them
- `execute_moves()`: Performs actual file operations with `shutil.move`
