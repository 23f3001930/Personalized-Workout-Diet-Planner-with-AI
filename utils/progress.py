import json
import os
from datetime import date

FILE = "progress.json"

def save_progress(weight):
    data = []
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            data = json.load(f)

    data.append({
        "date": str(date.today()),
        "weight": weight
    })

    with open(FILE, "w") as f:
        json.dump(data, f)

def load_progress():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []
