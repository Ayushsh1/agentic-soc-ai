from memory.memory import search_memory


# Step 1: Detection Agent
def detection_agent(alert):
    # Do NOT assign severity here
    return alert


# Step 2: Investigation Agent
def investigation_agent(alert):
    # Simulated threat intel
    alert["ip_reputation"] = "malicious"
    return alert


# Step 3: Decision Agent (CORE LOGIC 🔥)
def decision_agent(alert):
    # 🧠 Memory correlation
    memory_result = search_memory(alert["type"])
    alert["memory_match"] = memory_result

    # 🎯 Severity based on attack type
    if alert["type"] == "brute_force":
        alert["severity"] = "high"
    elif alert["type"] == "port_scan":
        alert["severity"] = "medium"
    else:
        alert["severity"] = "low"

    return alert


# Step 4: Response Agent
def response_agent(alert):
    if alert["severity"] == "high":
        alert["action"] = f"Blocked IP {alert['ip']}"
    elif alert["severity"] == "medium":
        alert["action"] = f"Flagged IP {alert['ip']} for monitoring"
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