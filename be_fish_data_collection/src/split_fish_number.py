import os
import cv2

INPUT_DIR = "square_images"
FISH_DIR = "fish_images"
NUMBER_DIR = "number_images"

os.makedirs(FISH_DIR, exist_ok=True)
os.makedirs(NUMBER_DIR, exist_ok=True)


def split_image(path):
    filename = os.path.basename(path)

    img = cv2.imread(path)

    if img is None:
        print(f"Failed to load {filename}")
        return

    h, w = img.shape[:2]

    # simple horizontal split
    fish_img = img[0:h // 2, 0:w]
    number_img = img[h // 2:h, 0:w]

    fish_path = os.path.join(FISH_DIR, filename)
    number_path = os.path.join(NUMBER_DIR, filename)

    cv2.imwrite(fish_path, fish_img)
    cv2.imwrite(number_path, number_img)

    print(f"Saved:")
    print(f"  Fish   -> {fish_path}")
    print(f"  Number -> {number_path}")
    print("-" * 40)


def main():
    files = os.listdir(INPUT_DIR)  # IMPORTANT: no sorting

    files = [
        f for f in files
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    if not files:
        print("No images found in square_debug")
        return

    for file in files:
        split_image(os.path.join(INPUT_DIR, file))

    print("\nDONE splitting images.")


if __name__ == "__main__":
    main()