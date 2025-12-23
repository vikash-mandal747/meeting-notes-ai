from typing import TypedDict, Optional


class MeetingState(TypedDict):
    transcript: Optional[str]
    cleaned_text: Optional[str]
    summary: Optional[str]
    action_items: Optional[list[str]]
