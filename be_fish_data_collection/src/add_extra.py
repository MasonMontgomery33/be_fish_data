import os

INPUT_FILE = "data/proper_data.txt"
OUTPUT_FILE = "data/data.txt"

RARITIES = [
    "Normal",
    "Gold",
    "Rainbow",
    "Glowing",
    "Shadow"
]

FISH_LIST = [
"Goldfish",
"Sardine",
"Tetra",
"Herring",
"Angelfish",
"Tilapia",
"Carp",
"Sheepshead",
"Starfish",
"Seahorse",
"Guppy",
"Tiger Barb",
"Bluegill",
"Clownfish",
"Parrotfish",
"Moorish Idol",
"Cichlid",
"Mackerel",
"Triggerfish",
"Trout",
"Piranha",
"Pufferfish",
"Jellyfish",
"Oscar",
"Fairy Wrasse",
"Catfish",
"Butterflyfish",
"Cod",
"Blue Tang",
"Flounder",
"Red Snapper",
"Salmon",
"Grouper",
"Stingray",
"Trevally",
"Betta Fish",
"Zebra Angelfish",
"Sunfish",
"Bass",
"Arowana",
"Pike",
"Barracuda",
"Zebra Shark",
"Nurse Shark",
"Humphead",
"Thresher Shark",
"Swordfish",
"Tuna",
"Anglerfish",
"Eagle Ray",
"Cobia",
"Sawfish",
"Hammerhead Shark",
"Mako Shark",
"Moonfish"
]


def main():

    if not os.path.exists(INPUT_FILE):
        print(f"Missing file: {INPUT_FILE}")
        return

    # ---------------- READ EXISTING DATA ----------------
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    existing = set(lines)

    output_lines = list(lines)

    # ---------------- ADD MISSING COMBINATIONS ----------------
    for rarity in RARITIES:
        for fish in FISH_LIST:

            combo_prefix = f"{rarity} {fish} "

            found = False

            for line in existing:
                if line.startswith(combo_prefix):
                    found = True
                    break

            if not found:
                output_lines.append(f"{rarity} {fish} 0")

    # ---------------- SAVE ----------------
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for line in output_lines:
            f.write(line + "\n")

    print("\n==============================")
    print("FINAL DATA COMPLETE")
    print(f"Saved: {OUTPUT_FILE}")
    print("==============================")


if __name__ == "__main__":
    main()