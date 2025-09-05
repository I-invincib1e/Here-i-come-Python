# Stopwatch CLI

A simple interactive stopwatch with laps.

## How to Run

- **Prerequisites**: Python 3.8+
- **Run**:
  - Windows PowerShell:
    - `python .\main.py`
  - macOS/Linux:
    - `python3 ./main.py`

## Commands

- `start`: Start or resume the stopwatch
- `lap`: Record a lap time
- `stop`: Pause and show elapsed time
- `reset`: Reset stopwatch and laps
- `exit`/`q`: Quit and show final time

## Lap Export

When you stop or exit the stopwatch, all recorded laps are automatically saved to a file named **`laps.csv`** in the same folder as the script.  

The file is **overwritten each time** you stop/exit.  

Example `laps.csv`:

```csv
lap_number,lap_time
1,00:01:23.123
2,00:01:45.456
3,00:02:10.789
  
## Demo

Placeholder for screenshot or GIF. Add your file under `docs/assets/` and link it here.


