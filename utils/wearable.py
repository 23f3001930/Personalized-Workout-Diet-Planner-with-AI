import random

def fetch_wearable_data():
    return {
        "steps": random.randint(4000, 12000),
        "calories_burned": random.randint(180, 600),
        "heart_rate": random.randint(60, 120)
    }
