def detect_threat(logs):
    alerts = []
    counter = {}

    for log in logs:
        if log["event"] == "failed_login":
            ip = log["ip"]
            counter[ip] = counter.get(ip, 0) + 1

            if counter[ip] > 2:
                alerts.append({"type": "brute_force", "ip": ip})

        elif log["event"] == "port_scan":
            alerts.append({"type": "port_scan", "ip": log["ip"]})

    return alerts