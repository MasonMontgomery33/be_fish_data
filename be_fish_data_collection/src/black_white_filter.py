import os
import numpy as np
from PIL import Image

KEEP_COLORS = [
    (69, 59, 49),
    (207, 174, 125)
]

THRESHOLD = 1

SCREENSHOT_DIR = "screenshots"
OUTPUT_DIR = "processed_images"

os.makedirs(OUTPUT_DIR, exist_ok=True)


# ---------------- FILTER IMAGE ----------------
def filter_image(image):
    img = np.array(image.convert("RGB"))

    mask = np.zeros(img.shape[:2], dtype=bool)

    for ref in KEEP_COLORS:
        dist = np.sqrt(np.sum((img - np.array(ref)) ** 2, axis=2))
        mask |= dist < THRESHOLD

    out = np.ones_like(img) * 255
    out[mask] = [0, 0, 0]

    return Image.fromarray(out.astype(np.uint8))


# ---------------- MAIN PROCESS ----------------
def process():
    files = sorted([
        f for f in os.listdir(SCREENSHOT_DIR)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ])

    if not files:
        print("No screenshots found.")
        return

    for i, file in enumerate(files):
        print(f"Processing {file}")

        path = os.path.join(SCREENSHOT_DIR, file)
        img = Image.open(path)

        filtered = filter_image(img)

        save_path = os.path.join(OUTPUT_DIR, f"processed_{i}_{file}")
        filtered.save(save_path)

        print(f"Saved: {save_path}")


if __name__ == "__main__":
    process()