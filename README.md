# meeting-notes-ai
Multi Agent Meeting Note Generator using LangGraph



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