from transcribe import transcribe_audio
from summarize import summarize_text

audio_path = "audio/sample.mp3"

print("Transcribing...")
text = transcribe_audio(audio_path)

print("\n--- TRANSCRIPTION ---")
print(text)

print("\nSummarizing...")
summary = summarize_text(text)

print("\n--- SUMMARY ---")
print(summary)
