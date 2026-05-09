import os

INPUT_FILE = "data/combined_data.txt"
OUTPUT_FILE = "data/rarity_data.txt"

RARITIES = [
    "Normal",
    "Gold",
    "Rainbow",
    "Glowing",
    "Shadow"
]


def main():

    if not os.path.exists(INPUT_FILE):
        print(f"Missing file: {INPUT_FILE}")
        return

    # ---------------- READ FILE ----------------
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    # tracks how many times we've seen each fish
    fish_counts = {}

    # keep output aligned in original order
    output = [None] * len(lines)

    # ---------------- BOTTOM -> TOP ----------------
    for i in range(len(lines) - 1, -1, -1):

        line = lines[i]

        parts = line.rsplit(" ", 1)

        if len(parts) != 2:
            print(f"Skipping invalid line: {line}")
            continue

        fish_name, number = parts

        # how many times we've already seen this fish
        count = fish_counts.get(fish_name, 0)

        # rarity based on occurrence
        rarity_index = min(count, len(RARITIES) - 1)

        rarity = RARITIES[rarity_index]

        # save result
        output[i] = f"{rarity} {fish_name} {number}"

        # increment count
        fish_counts[fish_name] = count + 1

    # ---------------- SAVE ----------------
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for line in output:
            if line:
                f.write(line + "\n")

    print("\n==============================")
    print("RARITY CALCULATION COMPLETE")
    print(f"Saved: {OUTPUT_FILE}")
    print("==============================")


if __name__ == "__main__":
    main()