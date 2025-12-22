from agents.transcriber import TranscriptionAgent


def main():
    print("🎙️ Transcribing meeting audio...")

    agent = TranscriptionAgent()
    text = agent.run("data/sample.wav")

    print("\n📝 Transcript:\n")
    print(text)


if __name__ == "__main__":
    main()
