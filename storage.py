import json

# File name for saving habits.
FILE_NAME = "habits.json"

# Save list of habit dicts to JSON.
def save(habits):
    with open(FILE_NAME, "w") as file:
        json.dump(habits, file, indent=4)  # Indent for readability

# Load JSON or return empty if no file.
def load():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # New start if no data