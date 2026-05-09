import os

NAMES_FILE = "data/fish_output.txt"
NUMBERS_FILE = "data/numbers.txt"
OUTPUT_FILE = "data/combined_data.txt"


def clean_number(text):
    """
    Convert OCR text into integer.
    Invalid values become 0.
    """

    text = str(text).strip()

    if text == "":
        return 0

    digits = ''.join(c for c in text if c.isdigit())

    if digits == "":
        return 0

    return int(digits)


def main():

    if not os.path.exists(NAMES_FILE):
        print(f"Missing file: {NAMES_FILE}")
        return

    if not os.path.exists(NUMBERS_FILE):
        print(f"Missing file: {NUMBERS_FILE}")
        return

    # ---------------- READ FILES ----------------
    with open(NAMES_FILE, "r", encoding="utf-8") as f:
        names = [line.strip() for line in f]

    with open(NUMBERS_FILE, "r", encoding="utf-8") as f:
        numbers = [line.strip() for line in f]

    # ---------------- MATCH TOP TO BOTTOM ----------------
    length = min(len(names), len(numbers))

    combined = []

    for i in range(length):

        fish = names[i]
        number = clean_number(numbers[i])

        # skip empty fish names
        if fish == "":
            continue

        combined.append(f"{fish} {number}")

    # ---------------- SAVE ----------------
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        for line in combined:
            f.write(line + "\n")

    print("\n==============================")
    print("DATA PROCESSING COMPLETE")
    print(f"Saved: {OUTPUT_FILE}")
    print("==============================")


if __name__ == "__main__":
    main()