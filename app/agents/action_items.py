import re


class ActionItemsAgent:
    def run(self, text: str) -> list[str]:
        actions = []
        lines = re.split(r"[.]", text)

        for line in lines:
            if any(word in line for word in ["need to", "should", "will", "action"]):
                actions.append(line.strip())

        return actions
