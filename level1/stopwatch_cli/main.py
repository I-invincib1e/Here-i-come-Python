import time
from typing import Optional


def format_duration(seconds: float) -> str:
    minutes, sec = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    millis = int((seconds - int(seconds)) * 1000)
    return f"{hours:02}:{minutes:02}:{sec:02}.{millis:03}"


def stopwatch() -> None:
    print("Stopwatch CLI")
    print("Commands: 'start' | 'lap' | 'stop' | 'reset' | 'exit'\n")
    start_time: Optional[float] = None
    elapsed: float = 0.0
    laps = []

    while True:
        cmd = input("> ").strip().lower()
        now = time.perf_counter()

        if cmd == "start":
            if start_time is None:
                start_time = now
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
        elif cmd == "stop":
            if start_time is None:
                print("Not running.")
            else:
                elapsed += now - start_time
                start_time = None
                print(f"Stopped at {format_duration(elapsed)}")
        elif cmd == "reset":
            start_time = None
            elapsed = 0.0
            laps.clear()
            print("Reset.")
        elif cmd in {"exit", "quit", "q"}:
            if start_time is not None:
                elapsed += now - start_time
                start_time = None
            print(f"Final time: {format_duration(elapsed)}")
            break
        else:
            print("Unknown command.")


if __name__ == "__main__":
    stopwatch()


