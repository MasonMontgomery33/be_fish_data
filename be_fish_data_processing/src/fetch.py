import json
import csv
from src.fish import Fish

def fetch_data(fish_dict):
    with open("data/data.json", "r") as f:
        data = json.load(f)

        for name, attrs in data.items():
            fish = Fish(
                type=attrs["type"],
                rarity=attrs["rarity"],
                level=(attrs["level"]),
                growth=float(attrs["growth"]),
                speed=float(attrs["speed"]),
                adj_speed=float(attrs["adj_speed"]),
                odds=float(attrs["odds"]),
                xp=float(attrs["xp"]),
                loot_efficiency=float(attrs["loot_efficiency"]),
                amount=int(attrs["amount"]),
                have=bool(attrs["have"]),
                projected_amount=int(attrs["projected_amount"])
            )

            fish_dict[name] = fish

def input_raw_values(fish_dict):
    for key in fish_dict:
        amount = input("How Many " + key + " do you have? ")
        try:
            value = int(amount)
        except ValueError:
            print("Invalid input: please enter a whole number.")
            continue

        # Step 2: check if it's non-negative
        if value < 0:
            print("Value must be greater than or equal to 0.")
            continue

        # Step 3: valid case
        print("Valid input received.")
        if (value > 0):
            fish_dict[key].set_have(True)
            fish_dict[key].set_amount(value)
        else:
            fish_dict[key].set_have(True)
            fish_dict[key].set_amount(value)

def input_command_values(fish_dict):
    with open("current_amounts.txt", "r") as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue  # skip empty lines and comments

            parts = line.split()

            if len(parts) < 2:
                print(f"Skipping invalid line: {line}")
                continue

            # everything except last word = fish name
            name = " ".join(parts[:-1])
            value_str = parts[-1]

            try:
                value = int(value_str)
            except ValueError:
                print(f"Invalid number for {name}: {value_str}")
                continue

            if value < 0:
                print(f"Value must be >= 0 for {name}")
                continue

            # normalize name to match your dict keys
            name = name.title().strip()

            if name not in fish_dict:
                print(f"Fish not found: {name}")
                continue

            fish_dict[name].set_have(value > 0)
            fish_dict[name].set_amount(value)

            print(f"Updated {name}: {value}")
            
def get_all_data(fish_dict):
    fetch_data(fish_dict)
    check = False
    while(check == False):
        choice = input("Type f for File Input and u For User Input Type s to Skip and Use Previous Input: ").lower()
        print(choice)
        if(choice == "u"):
            print("User Input:")
            input_raw_values(fish_dict)
            check = True
        elif(choice == "f"):
            print("File Input:")
            input_command_values(fish_dict)
            check = True
        elif(choice == "s"):
            print("Skipping Input...")
            check = True
        else:
            print("Wrong input")
#Rarity	Level	Growth	Speed	Adj. Speed	Odds	XP	Loot Effeciency	Concatination	Have
#Common	Normal	1	1	1	5	1	1	Normal Goldfish	x