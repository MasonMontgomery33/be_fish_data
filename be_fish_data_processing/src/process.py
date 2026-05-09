from src.constants import unique_fish_types
from src.fish import Fish
def display(fish_dict):
    for key in fish_dict:
        print(fish_dict[key].type + " Amount: " + str(fish_dict[key].amount))

def total(fish_dict):
    sum = 0
    for fish in unique_fish_types:
        sum += fish_pulled(fish_dict, fish)
    return sum
    
def fish_pulled(fish_dict, fish):
    fish = fish.title()
    if (("Normal " + fish) not in fish_dict):
        print("fish not found")
        return -1
    normal = int(fish_dict["Normal " + fish].amount)
    gold = int(fish_dict["Gold " + fish].amount) * 50
    rainbow = int(fish_dict["Rainbow " + fish].amount) * 50 * 50
    glowing = int(fish_dict["Glowing " + fish].amount) * 50 * 50 * 50
    shadow = int(fish_dict["Shadow " + fish].amount) * 50 * 50 *50 * 50
    
    sum = normal + gold + rainbow + glowing + shadow
    
    return sum

def fish_pulled_list(fish_dict):
    vec = []
    for fish in unique_fish_types:
        vec.append(fish_pulled(fish_dict, fish))
    return vec

def projected_amount(fish_dict, fish):
    words = fish.split(None, 1)
    fish_type = words[1]
    fish_total = fish_pulled(fish_dict, fish_type)
    total_fish = total(fish_dict)
    fraction = (fish_total)/(total_fish)
    if (fraction == 0):
        return 1000000000000000000000
    
    prestige = words[0]
    
    if(prestige == "Normal"):
        return 1/fraction
    elif(prestige == "Gold"):
        return 50/fraction
    elif(prestige == "Rainbow"):
        return 2500/fraction
    elif(prestige == "Glowing"):
        return 125000/fraction
    else:
        return 6250000/fraction

def projected_amount_list(fish_dict):
    sorted_fish = sorted(fish_dict.values(), key=lambda f: f.projected_amount)
    return sorted_fish

def xp_list(fish_dict):
    sorted_fish = sorted(fish_dict.values(), key=lambda f: f.loot_efficiency)
    return sorted_fish

def effeciency_list(fish_dict):
    projected = projected_amount_list(fish_dict)
    list = []
    max = 0
    for fish in projected:
        if(fish.loot_efficiency > max):
            max = fish.loot_efficiency
            list.append(fish)
    return list

def best_fish(fish_dict):
    xp = xp_list(fish_dict)
    vec = []
    for new_fish in xp:
        if(new_fish.have):
            vec.append(new_fish)
    return vec[-1]

def rarity_breakdown(fish_dict):
    rarity_sums = {
    "Common": 0,
    "Uncommon": 0,
    "Rare": 0,
    "Epic": 0,
    "Legendary": 0,
    "Total": 0
    }
    
    for key, fish in fish_dict.items():
        words = key.split(None, 1)
        fish_type = words[1]
        pulled = fish_pulled(fish_dict, fish_type)
        rarity = fish.rarity

        if rarity not in rarity_sums:
            rarity = "Legendary"

        rarity_sums[rarity] += pulled
        rarity_sums["Total"] += pulled
    
    print("Common Percentage: " + str(rarity_sums["Common"]/rarity_sums["Total"] * 100))
    print("")
    print()
    print("Uncommon Percentage: " + str(rarity_sums["Uncommon"]/rarity_sums["Total"] * 100))
    print("Rare Percentage: " + str(rarity_sums["Rare"]/rarity_sums["Total"] * 100))
    print("Epic Percentage: " + str(rarity_sums["Epic"]/rarity_sums["Total"] * 100))
    print("Legendary Percentage: " + str(rarity_sums["Legendary"]/rarity_sums["Total"] * 100))
            