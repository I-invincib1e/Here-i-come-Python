# Text to Speech Converter

A simple command-line text-to-speech converter that simulates speech output.

## Features

- Convert text to simulated speech
- Adjustable speaking speed (0.5x to 2.0x)
- Word-by-word output with timing
- Interactive CLI interface

## Usage

```bash
python main.py
```

Enter text and optionally adjust the speaking speed.

## How it Works

This is a simulation that:
- Splits text into words
- Prints each word with a speaker emoji
- Adds delays based on word length and speed setting
- Provides visual feedback of the "speech" process

## Note

This is a basic simulation for demonstration. For real text-to-speech, you would use libraries like:
- pyttsx3
- gTTS (Google Text-to-Speech)
- speech_recognition

## Requirements

- Python 3.6+
- No external dependencies (simulation only)
