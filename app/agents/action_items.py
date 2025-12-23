import re


class ActionItemsAgent:
    def run(self, text: str) -> list[str]:
        actions = []
        lines = re.split(r"[.]", text)

        keywords = [
            "need to",
            "should",
            "will",
            "let's",
            "we have to",
            "plan to",
            "decide to",
        ]

        for line in lines:
            if any(k in line for k in keywords):
                actions.append(line.strip())

        return actions
