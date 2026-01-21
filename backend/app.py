from fastapi import FastAPI, UploadFile , File
from services.ocr import extract_text
from fastapi.middleware.cors import CORSMiddleware
from services.llm import call_llm
from utils.prompts import simplify_prompt, question_prompt
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="AI Assistive Reader Backend")


app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return{"status" : "AI Assistive Reader backend is running ... "}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    text = await extract_text(file)
    return {"extracted_text": text}


@app.post("/summarize")
async def summarize(payload: dict):

    if "text" not in payload:
        return {"error" : "text is required"}

    text = payload["text"]
    language = payload.get("language", "English")

    prompt = simplify_prompt(text, language)
    summary = call_llm(prompt)

    return {"summary": summary}


@app.post("/ask")
async def ask_question(payload: dict):
    
    if "summary" not in payload or "question" not in payload:
        return{"error" : "summary and question are required"}
    
    summary = payload["summary"]
    question = payload["question"]
    language = payload.get("language", "English")

    prompt = question_prompt(summary, question, language)
    answer = call_llm(prompt)

    return {"answer": answer}
