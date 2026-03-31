import json

def map_mitre(alert):
    with open("mitre/map.json") as f:
        data = json.load(f)

    alert.update(data.get(alert["type"], {}))
    return alert