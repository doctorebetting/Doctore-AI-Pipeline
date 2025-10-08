import json

def load_endpoints(path="config/espn_endpoints.json"):
    with open(path) as f:
        return json.load(f)