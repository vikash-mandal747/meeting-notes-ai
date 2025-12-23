class SummarizerAgent:
    def run(self, text: str) -> str:
        sentences = text.split(".")
        return ". ".join(sentences[:3]).strip() + "."
