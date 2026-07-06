from faster_whisper import WhisperModel
from pathlib import Path
import os
import time

AUDIO_FILE = "test.wav"

if not os.path.exists(AUDIO_FILE):
    print(f"Error: File {AUDIO_FILE} not found!")
    exit(1)

print(f"File: {AUDIO_FILE}")
print(f"Size: {os.path.getsize(AUDIO_FILE) / 1024:.1f} KB")
print("\nLoading model...")

model = WhisperModel(
    "medium",
    device="cpu",
    compute_type="int8"
)

print("Model loaded successfully.")
print("\nProcessing audio...")

start_time = time.time()

segments, info = model.transcribe(
    AUDIO_FILE,
    language="fa",
    vad_filter=True,
    vad_parameters=dict(min_silence_duration_ms=500)
)

text = ""
print(f"\nDetected Language: {info.language} (Probability: {info.language_probability:.2f})")
print("\n--- Output Text ---\n")

for segment in segments:
    # print(segment.text)
    text += segment.text + "\n"

elapsed = time.time() - start_time

Path("output.txt").write_text(text, encoding="utf-8")

print(f"\nText saved to output.txt")
print(f"Processing time: {elapsed:.1f} seconds")