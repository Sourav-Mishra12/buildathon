# AI Assistive Reader

An AI-powered tool that helps users understand complex documents by:
- Extracting text from images (OCR)
- Generating a simplified English summary
- Answering user questions
- Reading the content aloud in multiple languages (English / Hindi)

Built as a hackathon MVP with a focus on accessibility and clarity.

---

## 🚀 Features
- Image-based document upload (OCR)
- Simple English summary generation
- Question & Answer on the document
- Text-to-Speech with language & speed control
- Offline-friendly local LLM using Ollama (Llama 3 – 8B)

---

## 🛠 Tech Stack
- **Backend:** FastAPI, Python
- **OCR:** Tesseract OCR
- **LLM:** Llama 3 (8B) via Ollama
- **Frontend:** HTML, CSS, Vanilla JavaScript
- **TTS:** Browser Web Speech API

---

## ▶️ How to Run (Local)

### 1. Start Backend
```bash
cd backend
uvicorn app:app --reload
