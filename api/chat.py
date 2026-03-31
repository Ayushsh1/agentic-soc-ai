from fastapi import APIRouter
from memory.memory import search_memory
import datetime

router = APIRouter()

@router.get("/chat")
def chat(query: str):
    memory = search_memory(query)

    # Explanation logic
    if "brute" in query:
        explanation = "This is a brute force attack where multiple login attempts are made."
    elif "port" in query:
        explanation = "This indicates a port scanning activity to discover open ports."
    else:
        explanation = "General suspicious activity detected."

    return {
        "alert_type": query,
        "timestamp": str(datetime.datetime.now()),
        "analysis": {
            "explanation": explanation,
            "similar_incident": memory,
            "risk_level": "HIGH"
        },
        "recommended_action": "Block the IP and monitor for further suspicious activity."
    }