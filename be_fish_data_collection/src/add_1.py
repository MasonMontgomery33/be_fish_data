import os

INPUT_FILE = "data/rarity_data.txt"
OUTPUT_FILE = "data/proper_data.txt"


def main():

    if not os.path.exists(INPUT_FILE):
        print(f"Missing file: {INPUT_FILE}")
        return

    updated_lines = []

    # ---------------- READ + UPDATE ----------------
    with open(INPUT_FILE, "r", encoding="utf-8") as f:

        for line in f:

            line = line.strip()

            if not line:
                continue

            parts = line.rsplit(" ", 1)

            # must end with a number
            if len(parts) != 2:
                print(f"Skipping invalid line: {line}")
                continue

            left_side, number = parts

            try:
                new_number = int(number) + 1
            except ValueError:
                print(f"Skipping invalid number: {line}")
                continue

            updated_lines.append(f"{left_side} {new_number}")

    # ---------------- SAVE ----------------
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for line in updated_lines:
            f.write(line + "\n")

    print("\n==============================")
    print("NUMBER UPDATE COMPLETE")
    print(f"Saved: {OUTPUT_FILE}")
    print("==============================")


if __name__ == "__main__":
    main()