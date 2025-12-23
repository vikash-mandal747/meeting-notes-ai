import re


class CleanerAgent:
    def run(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"\b(um+|uh+|you know|like)\b", "", text)
        text = re.sub(r"\s+", " ", text)
        return text.strip()
