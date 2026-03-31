from memory.memory import search_memory

# Step 1: Detection Agent
def detection_agent(alert):
    alert["severity"] = "medium"
    return alert


# Step 2: Investigation Agent
def investigation_agent(alert):
    # Simulated threat intel
    alert["ip_reputation"] = "malicious"
    return alert


# Step 3: Decision Agent (WITH MEMORY 🔥)
def decision_agent(alert):
    # Use memory to find similar past incidents
    memory_result = search_memory(alert["type"])
    
    alert["memory_match"] = memory_result

    # Decision logic
    if alert["ip_reputation"] == "malicious":
        alert["severity"] = "high"

    return alert


# Step 4: Response Agent
def response_agent(alert):
    if alert["severity"] == "high":
        alert["action"] = f"Blocked IP {alert['ip']}"
    else:
        alert["action"] = "Monitor"

    return alert


# Full Pipeline
def run_pipeline(alert):
    alert = detection_agent(alert)
    alert = investigation_agent(alert)
    alert = decision_agent(alert)
    alert = response_agent(alert)
    return alert