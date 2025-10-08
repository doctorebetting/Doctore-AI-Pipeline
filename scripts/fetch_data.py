import requests
import json
from datetime import datetime

def load_endpoints(path="config/espn_endpoints.json"):
    import os, json
    with open(path) as f:
        return json.load(f)

def fetch_and_save(sport_key, endpoint_url):
    resp = requests.get(endpoint_url)
    date_str = datetime.utcnow().strftime("%Y%m%d")
    filename = f"data/raw/{date_str}_{sport_key}.json"
    with open(filename, "w") as f:
        json.dump(resp.json(), f)
    return resp.json()

def main():
    endpoints = load_endpoints()
    for sport, cfg in endpoints.items():
        if "scores" in cfg:
            fetch_and_save(sport + "_scores", cfg["scores"])
        # optionally fetch team, news also
    print("Fetch complete.")

if __name__ == "__main__":
    main()