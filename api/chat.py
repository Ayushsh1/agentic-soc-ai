from fastapi import APIRouter
from memory.memory import search_memory
from datetime import datetime

router = APIRouter()

@router.get("/chat")
def chat(query: str):
    query = query.lower()  # 🧠 normalize input
    memory = search_memory(query)

    # 🧠 Explanation + Risk logic
    if "brute" in query:
        explanation = "This is a brute force attack where multiple login attempts are made."
        risk = "HIGH"
        action = "Block the IP immediately and enforce account lockout policies."
    elif "port" in query:
        explanation = "This indicates a port scanning activity to discover open ports."
        risk = "MEDIUM"
        action = "Monitor the IP and consider blocking if repeated activity is observed."
    else:
        explanation = "General suspicious activity detected."
        risk = "LOW"
        action = "Monitor the activity and analyze logs for anomalies."

    # 🔥 Confidence score (adds AI feel)
    confidence = 0.9 if risk == "HIGH" else 0.7 if risk == "MEDIUM" else 0.5

    return {
        "alert_type": query,
        "timestamp": datetime.now().isoformat(),  # cleaner format
        "analysis": {
            "explanation": explanation,
            "similar_incident": memory,
            "risk_level": risk,
            "confidence_score": confidence
        },
        "recommended_action": action
    }