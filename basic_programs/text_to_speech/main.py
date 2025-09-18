#!/usr/bin/env python3
"""
Text to Speech - CLI
A simple text-to-speech converter (simulated).
"""

import time
import random

def speak_text(text, speed=1.0):
    """Simulate text-to-speech by printing words with delays."""
    words = text.split()
    print(f"\nSpeaking at speed {speed}x:")
    print("-" * 40)

    for word in words:
        print(f"🔊 {word}")
        # Simulate speaking time based on word length
        delay = len(word) * 0.1 / speed
        time.sleep(delay)

    print("-" * 40)
    print("Speech completed!")

def main():
    print("Text to Speech Converter")
    print("-" * 30)

    while True:
        text = input("Enter text to speak (or 'quit' to exit): ").strip()

        if text.lower() == 'quit':
            break

        if text:
            try:
                speed = float(input("Enter speaking speed (0.5-2.0, default 1.0): ") or 1.0)
                speed = max(0.5, min(2.0, speed))  # Clamp between 0.5 and 2.0
                speak_text(text, speed)
            except ValueError:
                print("Invalid speed. Using default speed 1.0")
                speak_text(text)
        else:
            print("Please enter some text.")

    print("Goodbye!")

if __name__ == "__main__":
    main()
