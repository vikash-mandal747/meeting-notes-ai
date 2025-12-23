# meeting-notes-ai
Multi Agent Meeting Note Generator using LangGraph


installed dependency --> python -m pip install langgraph langchain python-dotenv faster-whisper



faster_whisper model [for audio transcribe]




Architecture:
Audio
  ↓
Transcriber Agent (faster_whisper)
  ↓
Cleaner Agent
  ↓
Summarizer Agent (LLM)
  ↓
Action Items Agent
  ↓
Structured Output

(LangGraph controls who runs when.)





Hugging Face Summarizer:
dependency:
pip install transformers torch sentencepiece

torch (The Engine)
PyTorch is the "math engine." It’s the foundation that handles all the heavy lifting (matrix multiplications) required for neural networks to work.

transformers (The Model Library)
Created by Hugging Face, this library is like a giant "App Store" for AI models. It allows you to download, load, and run thousands of pre-trained models with just two lines of code.

sentencepiece (The Translator)
Computers don't understand words; they understand numbers. SentencePiece is a "Tokenizer." Its job is to break your sentences into tiny chunks (tokens) and turn them into a list of numbers that the AI model can understand.

