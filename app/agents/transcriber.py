from faster_whisper import WhisperModel
from pathlib import Path


class TranscriptionAgent:
    def __init__(self, model_size="small"):
        self.model = WhisperModel(
            model_size,
            device="cpu",
            compute_type="int8"
        )

    def run(self, audio_path: str) -> str:
        audio = Path(audio_path)

        if not audio.exists():
            raise FileNotFoundError(f"Audio not found: {audio_path}")

        segments, _ = self.model.transcribe(str(audio))
        return " ".join(seg.text.strip() for seg in segments)
