from fastapi import FastAPI
import json

from detection.detect import detect_threat
from agents.pipeline import run_pipeline
from mitre.map import map_mitre
from api.chat import router as chat_router

app = FastAPI()

app.include_router(chat_router)


@app.get("/")
def home():
    return {"message": "Agentic SOC Running"}

@app.get("/run")
def run():
    with open("logs/sample_logs.json") as f:
        logs = json.load(f)

    alerts = detect_threat(logs)

    results = []
    for alert in alerts:
        alert = run_pipeline(alert)
        alert = map_mitre(alert)
        results.append(alert)

    return results