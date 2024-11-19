import json

def save_grid(grid, filename="data/save.json"):
    with open(filename, "w") as file:
        json.dump(grid, file)

def load_grid(filename="data/save.json"):
    with open(filename, "r") as file:
        return json.load(file)