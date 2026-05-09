import os
import cv2
import numpy as np
import re

TEMPLATE_DIR = "templates_normalized"
INPUT_DIR = "number_images"
OUTPUT_FILE = "data/numbers.txt"


# ---------------- LOAD TEMPLATES ----------------
def load_templates():
    templates = {}

    files = sorted([
        f for f in os.listdir(TEMPLATE_DIR)
        if f.lower().endswith(".png")
    ])

    for f in files:
        digit = os.path.splitext(f)[0]

        img = cv2.imread(os.path.join(TEMPLATE_DIR, f), cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue

        _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

        templates[digit] = img

    return templates


# ---------------- PREPROCESS IMAGE ----------------
def preprocess(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # invert so digits become white
    _, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY_INV)

    return thresh


# ---------------- FIND DIGIT BOXES ----------------
def get_digit_boxes(thresh):

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    boxes = []

    for c in contours:
        x, y, w, h = cv2.boundingRect(c)

        if w < 4 or h < 4:
            continue

        boxes.append((x, y, w, h))

    boxes.sort(key=lambda b: b[0])  # left → right

    return boxes


# ---------------- NORMALIZE DIGIT ----------------
def normalize_digit(img):
    return cv2.resize(img, (64, 64))


# ---------------- MATCH DIGIT ----------------
def match_digit(img, templates):

    best_digit = None
    best_score = -1

    for digit, template in templates.items():

        t = cv2.resize(template, (64, 64))

        res = cv2.matchTemplate(img, t, cv2.TM_CCOEFF_NORMED)
        score = res[0][0]

        if score > best_score:
            best_score = score
            best_digit = digit

    return best_digit


# ---------------- READ NUMBER ----------------
def read_number(img, templates):

    thresh = preprocess(img)

    boxes = get_digit_boxes(thresh)

    if not boxes:
        return 0

    result = ""

    for (x, y, w, h) in boxes:

        digit_img = thresh[y:y+h, x:x+w]
        digit_img = normalize_digit(digit_img)

        digit = match_digit(digit_img, templates)

        if digit is not None:
            result += str(digit)

    return int(result) if result else 0


# ---------------- ORDERING SYSTEM (IMPORTANT FIX) ----------------
def extract_order_key(filename):
    """
    processed_<A>_..._square_<B>.png
    sorts by (A, B)
    """

    match = re.search(r"processed_(\d+).*_square_(\d+)", filename)

    if not match:
        return (999999, 999999)

    return (int(match.group(1)), int(match.group(2)))


# ---------------- MAIN ----------------
def main():

    os.makedirs("data", exist_ok=True)

    templates = load_templates()

    files = [
        f for f in os.listdir(INPUT_DIR)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    # ✅ CRITICAL FIX: correct processing order
    files.sort(key=extract_order_key)

    results = []

    for f in files:

        path = os.path.join(INPUT_DIR, f)
        img = cv2.imread(path)

        if img is None:
            continue

        number = read_number(img, templates)

        print(f"{f} -> {number}")

        results.append((f, number))

    # ---------------- SAVE OUTPUT ----------------
    with open(OUTPUT_FILE, "w") as out:
        for f, num in results:
            out.write(f"{num}\n")

    print("\nDONE")
    print(f"Saved: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()