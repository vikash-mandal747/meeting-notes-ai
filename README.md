# meeting-notes-ai
Multi Agent Meeting Note Generator using LangGraph


installed dependency --> python -m pip install langgraph langchain python-dotenv faster-whisper



faster_whisper model [for audio transcribe]




Architecture:
Audio
  ↓
Transcriber Agent
  ↓
Cleaner Agent
  ↓
Summarizer Agent
  ↓
Action Items Agent
  ↓
Structured Output

(LangGraph controls who runs when.)