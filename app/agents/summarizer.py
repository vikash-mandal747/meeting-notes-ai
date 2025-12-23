from transformers import pipeline


class SummarizerAgent:
    def __init__(self):
        self.summarizer = pipeline(
            "summarization",
            model="facebook/bart-large-cnn",
            device=-1  # CPU only
        )

    def run(self, text: str) -> str:
        if len(text) < 100:
            return text

        result = self.summarizer(
            text,
            max_length=150,
            min_length=50,
            do_sample=False
        )

        return result[0]["summary_text"]
