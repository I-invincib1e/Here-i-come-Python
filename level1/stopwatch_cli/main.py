import time
from typing import Optional
import csv
import os
# Export laps to a CSV file
def lap_export(laps):
    script_dir = os.path.dirname(os.path.abspath(__file__))  # folder where script is
    file_path = os.path.join(script_dir, "laps.csv")         # laps.csv in same folder
    # print(f"Saving laps to: {file_path}")   To check where file is saved
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["lap_number", "lap_time"])  # header
        for i, lap in enumerate(laps):
            writer.writerow([i + 1, format_duration(lap)])


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
                # Export laps to CSV on stop
                lap_export(laps)
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
            lap_export(laps)
            print(f"Final time: {format_duration(elapsed)}")
            break
        else:
            print("Unknown command.")


if __name__ == "__main__":
    stopwatch()


