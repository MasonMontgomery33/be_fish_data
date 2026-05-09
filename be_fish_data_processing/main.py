from src.fish import Fish
from src.fetch import fetch_data
from src.fetch import get_all_data
from src.storage import update
from src.process import *
from src.constants import unique_fish_types


fish_dict = {}
get_all_data(fish_dict)
update(fish_dict)

while True:
    print("\n=== MAIN MENU ===")
    print("1. Extras")
    print("2. View Lists")
    print("3. Adjust Data")
    print("4. Exit")

    choice = input("Select an option: ").strip()

    # Extras Section
    if choice == "1":
        print("\n--- EXTRAS ---")
        print("1. View Total Fish Collected (Includes Treasure Chests)")
        print("2. View Best Fish")
        print("3. Fish Data Access")
        print("4. Rarity Breakdown")

        extra_choice = input("Choose an extra option: ").strip()

        if extra_choice == "1":
            print("Running Total Fish...")
            print("Total Fish Pulled: " + str(total(fish_dict)))

        elif extra_choice == "2":
            print("Running Best Fish...")
            print("Best Fish: " + str(best_fish(fish_dict).type))
        
        elif(extra_choice == "3"):
            print("Running Fish Data...")
            fish_choice = input("Choose a fish: ")
            fish_choice = fish_choice.title()
            if fish_choice not in fish_dict:
                print("Not a fish")
            else:
                print(fish_dict[fish_choice])

        elif(extra_choice == "4"):
            rarity_breakdown(fish_dict)

        else:
            print("Invalid extra option")

    # List Display Section
    elif choice == "2":
        print("\n--- LIST OPTIONS ---")
        print("1. Fish Species Amount Pulled List")
        print("2. Projected Amount of Fish to Collect To Unlock List")
        print("3. Sorted List of Fish by Loot Effeciency")
        print("4. Most Effecient Path of Fish List (Subject to Change With Luck)")
        print("5. Blank")

        list_choice = input("Choose a list: ").strip()

        if list_choice == "1":
            print("Displaying Fish Species Amount List...")
            amounts = fish_pulled_list(fish_dict)
            for species, amount in zip(unique_fish_types, amounts):
                print(species + " - Amount: " + str(amount))
        elif list_choice == "2":
            print("Displaying Projected List...")
            for key in fish_dict:
                print(fish_dict[key].type + " - Projection: " + str(fish_dict[key].projected_amount))

        elif list_choice == "3":
            print("Displaying Loot Effeciency List...")
            list = xp_list(fish_dict)
            for fish in list:
                print(f"{fish.type} - Efficiency: {str(fish.loot_efficiency)} {"- ✓" if fish.have else "- x"}")

        elif list_choice == "4":
            print("Displaying Most Effecienct Path...")
            list = effeciency_list(fish_dict)
            for fish in list:
                print(f"{fish.type} - Efficiency: {fish.loot_efficiency} - Odds: {fish.projected_amount} {'- ✓' if fish.have else '- x'}")

        elif list_choice == "5":
            print("Displaying List 5")

        else:
            print("Invalid list choice")

    # Adjustement section
    elif choice == "3":
        print("\n--- ADJUST OPTIONS ---")
        print("1. Adjust Singular Amount of Fish")
        print("2. Reset Fish Inventory")

        adjust_choice = input("Choose adjustment: ").strip()

        if adjust_choice == "1":
            print("Adjusting Singlunar Amount of Fish..")
            fish_choice = input("Choose fish: ")
            try:
                amount_choice = int(input("Choose new amount: ").strip())
            except ValueError:
                print("Invalid number")
                continue

            if amount_choice < 0:
                print(f"Value must be >= 0")
                continue
            
            fish_choice = fish_choice.title()
            if fish_choice not in fish_dict:
                print("Fish type not recognized.")
            else:
                fish_dict[fish_choice].amount = amount_choice
            update(fish_dict)

        elif adjust_choice == "2":
            print("Adjusting Entire Inventory...")
            get_all_data(fish_dict)
            update(fish_dict)

        else:
            print("Invalid adjustment choice")

    # Exit
    elif choice == "4":
        print("Exiting program.")
        update(fish_dict)
        break

    else:
        print("Invalid selection")