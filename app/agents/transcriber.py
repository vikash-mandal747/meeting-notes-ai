from faster_whisper import WhisperModel
import os

model = WhisperModel("small", device="cpu", compute_type="int8")


def transcribe_audio(audio_path: str) -> str:
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    segments, info = model.transcribe(audio_path)
    return " ".join(segment.text for segment in segments)
