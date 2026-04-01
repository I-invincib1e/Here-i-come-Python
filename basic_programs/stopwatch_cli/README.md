# Stopwatch CLI

A simple interactive stopwatch with laps.

## How It Works

- Maintains state: `start_time`, `elapsed`, and `laps`
- `start`: begins timing (idempotent)
- `lap`: records current total elapsed time
- `lap export`: writes laps to `laps.csv`
- `stop`: freezes time and accumulates into `elapsed`
- `reset`: clears time and laps
- `exit`/`q`: prints final time and quits

## Example

```text
> start
Started.
> lap
Lap 1: 00:00:02.153
> stop
Stopped at 00:00:04.302
> exit
Final time: 00:00:04.302
```

## Internals

- Uses `time.perf_counter()` for high-resolution timing
- Simple REPL loop handles commands and errors
