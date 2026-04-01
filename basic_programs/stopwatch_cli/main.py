import time
import csv
from typing import Optional

from shared.cli_utils import create_repl_loop


def format_duration(seconds: float) -> str:
    minutes, sec = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{sec:02}.{millis:03}"


def process_command(cmd: str, state: dict) -> None:
    now = time.perf_counter()
    start_time: Optional[float] = state.get("start_time")
    elapsed: float = state.get("elapsed", 0.0)
    laps = state.setdefault("laps", [])

    if cmd == "start":
        if start_time is None:
            state["start_time"] = now
            print("Started.")
        else:
            print("Already running.")
    elif cmd == "lap":
        if start_time is None:
            print("Start the stopwatch first.")
        else:
            current_elapsed = elapsed + (now - start_time)
            laps.append(current_elapsed)
            print(f"Lap {len(laps)}: {format_duration(current_elapsed)}")
    elif cmd == "lap export":
        if not laps:
            print("No laps to export.")
        else:
            with open("laps.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Lap", "Total Time", "Duration"])
                prev_total = 0.0
                for i, total in enumerate(laps, 1):
                    duration = total - prev_total
                    writer.writerow([i, f"{total:.3f}", f"{duration:.3f}"])
                    prev_total = total
            print("Laps exported to laps.csv.")
    elif cmd == "stop":
        if start_time is None:
            print("Not running.")
        else:
            elapsed += now - start_time
            state["elapsed"] = elapsed
            state["start_time"] = None
            print(f"Stopped at {format_duration(elapsed)}")
    elif cmd == "reset":
        state["start_time"] = None
        state["elapsed"] = 0.0
        laps.clear()
        print("Reset.")
    elif cmd in {"exit", "quit", "q"}:
        if start_time is not None:
            elapsed += now - start_time
            state["elapsed"] = elapsed
            state["start_time"] = None
        print(f"Final time: {format_duration(elapsed)}")
        raise SystemExit
    else:
        print("Unknown command.")


def repl() -> None:
    print("Stopwatch CLI")
    print("Commands: 'start' | 'lap' | 'stop' | 'reset' | 'exit'\n")
    state = {"start_time": None, "elapsed": 0.0, "laps": []}

    def handler(line: str) -> None:
        process_command(line.strip().lower(), state)

    try:
        create_repl_loop(handler, "", "> ")
    except SystemExit:
        pass


if __name__ == "__main__":
    repl()


