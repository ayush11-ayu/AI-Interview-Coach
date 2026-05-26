from fastapi import FastAPI
from backend.ai_engine import analyze_resume, generate_questions, evaluate_answer

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Interview Coach Running"}

@app.post("/resume")
def resume_analysis(data: dict):
    result = analyze_resume(data["text"])
    return {"result": result}

@app.post("/questions")
def questions(data: dict):
    result = generate_questions(data["role"])
    return {"result": result}

@app.post("/evaluate")
def evaluate(data: dict):
    result = evaluate_answer(data["answer"])
    return {"result": result}