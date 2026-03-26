from fastapi import FastAPI
from pydantic import BaseModel
from detector import detect_sensitive_data
from risk_engine import calculate_risk
from ai_module import generate_insights
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Input(BaseModel):
    content: str

@app.get("/")
def home():
    return {"message": "Backend running 🚀"}

@app.post("/analyze")
def analyze(data: Input):
    lines = data.content.split("\n")

    findings = detect_sensitive_data(lines)
    score, level = calculate_risk(findings)
    insights = generate_insights(findings)

    return {
        "summary": "Log analyzed successfully",
        "findings": findings,
        "risk_score": score,
        "risk_level": level,
        "insights": insights
    }