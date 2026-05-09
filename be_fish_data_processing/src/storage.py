import json
from src.process import projected_amount

def update(fish_dict):
    for key in fish_dict:
        fish_dict[key].projected_amount = projected_amount(fish_dict, key)
    with open("data/data.json", "w") as f:
        data = {
            name: fish.to_dict()
            for name, fish in fish_dict.items()
        }

        json.dump(data, f, indent=4)