from agents.transcriber import transcribe_audio

if __name__ == "__main__":
    audio_path = "data/sample.wav"

    print("Transcribing audio...")
    text = transcribe_audio(audio_path)

    print("\n--- TRANSCRIPTION OUTPUT ---\n")
    print(text)
