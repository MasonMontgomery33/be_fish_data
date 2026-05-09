import os
import cv2
import pytesseract
import re
from difflib import get_close_matches

INPUT_DIR = "fish_images"
OUTPUT_DIR = "data"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "fish_output.txt")

os.makedirs(OUTPUT_DIR, exist_ok=True)


# ---------------- YOUR FISH LIST ----------------
FISH_LIST = [
    "Goldfish", "Sardine", "Tetra", "Herring", "Angelfish",
    "Tilapia", "Carp", "Sheepshead", "Starfish", "Seahorse",
    "Guppy", "Tiger Barb", "Bluegill", "Clownfish", "Parrotfish",
    "Moorish Idol", "Cichlid", "Mackerel", "Triggerfish", "Trout",
    "Piranha", "Pufferfish", "Jellyfish", "Oscar", "Fairy Wrasse",
    "Catfish", "Butterflyfish", "Cod", "Blue Tang", "Flounder",
    "Red Snapper", "Salmon", "Grouper", "Stingray", "Trevally",
    "Betta Fish", "Zebra Angelfish", "Sunfish", "Bass", "Arowana",
    "Pike", "Barracuda", "Zebra Shark", "Nurse Shark", "Humphead",
    "Thresher Shark", "Swordfish", "Tuna"
]


# ---------------- SORT KEY ----------------
def extract_keys(filename):
    match = re.search(r"processed_(\d+).*_square_(\d+)", filename)
    if not match:
        return (999999, 999999)
    return (int(match.group(1)), int(match.group(2)))


# ---------------- CLEAN TEXT ----------------
def clean(text):
    text = text.strip()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    text = " ".join(text.split())
    return text


# ---------------- MATCH AGAINST LIST ----------------
def match_fish(text):
    if not text:
        return None

    text = clean(text).lower()

    # exact match first
    for fish in FISH_LIST:
        if text == fish.lower():
            return fish

    # substring match
    for fish in FISH_LIST:
        if fish.lower() in text:
            return fish

    # fuzzy match (fix OCR mistakes like "Clownfih")
    match = get_close_matches(text, [f.lower() for f in FISH_LIST], n=1, cutoff=0.8)

    if match:
        for fish in FISH_LIST:
            if fish.lower() == match[0]:
                return fish

    return None


# ---------------- OCR ----------------
def ocr_fish(img):
    config = "--psm 7"
    text = pytesseract.image_to_string(img, config=config)
    return match_fish(text)


# ---------------- MAIN ----------------
def process():

    files = [
        f for f in os.listdir(INPUT_DIR)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    # correct reading order
    files.sort(key=extract_keys)

    results = []

    for file in files:

        path = os.path.join(INPUT_DIR, file)
        img = cv2.imread(path)

        if img is None:
            continue

        fish = ocr_fish(img)

        # 🔥 HARD FILTER: only allowed fish go through
        if fish is None:
            continue

        results.append(fish)

        print(f"{file} -> {fish}")

    # ---------------- SAVE ----------------
    with open(OUTPUT_FILE, "w") as f:
        for fish in results:
            f.write(f"{fish}\n")

    print("\nDONE")
    print(f"Saved: {OUTPUT_FILE}")


if __name__ == "__main__":
    process()