from langgraph.graph import StateGraph, END
from agents.transcriber import TranscriptionAgent
from agents.cleaner import CleanerAgent
from agents.summarizer import SummarizerAgent
from agents.action_items import ActionItemsAgent
from state import MeetingState


def build_meeting_graph():
    graph = StateGraph(MeetingState)

    transcriber = TranscriptionAgent()
    cleaner = CleanerAgent()
    summarizer = SummarizerAgent()
    action_agent = ActionItemsAgent()

    graph.add_node("transcribe", lambda s: {
        "transcript": transcriber.run("data/sample.wav")
    })

    graph.add_node("clean", lambda s: {
        "cleaned_text": cleaner.run(s["transcript"])
    })

    graph.add_node("summarize", lambda s: {
        "summary": summarizer.run(s["cleaned_text"])
    })

    graph.add_node("actions", lambda s: {
        "action_items": action_agent.run(s["cleaned_text"])
    })

    graph.set_entry_point("transcribe")
    graph.add_edge("transcribe", "clean")
    graph.add_edge("clean", "summarize")
    graph.add_edge("summarize", "actions")
    graph.add_edge("actions", END)

    return graph.compile()
