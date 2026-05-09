import os
import cv2

INPUT_DIR = "processed_images"
OUTPUT_DIR = "square_images"
DEBUG_DIR = "square_debug"

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(DEBUG_DIR, exist_ok=True)

# grid layout
COLS = 4
ROWS = 2


def process_image(path):

    filename = os.path.basename(path)

    print(f"Processing {filename}")

    img = cv2.imread(path)

    if img is None:
        print("Failed to load image")
        return

    height, width = img.shape[:2]

    # square size
    cell_width = width // COLS
    cell_height = height // ROWS

    # debug image
    debug = img.copy()

    square_num = 0

    for row in range(ROWS):
        for col in range(COLS):

            x1 = col * cell_width
            y1 = row * cell_height

            # make sure last row/col reaches edge
            if col == COLS - 1:
                x2 = width
            else:
                x2 = (col + 1) * cell_width

            if row == ROWS - 1:
                y2 = height
            else:
                y2 = (row + 1) * cell_height

            # crop square
            square = img[y1:y2, x1:x2]

            # save square
            square_path = os.path.join(
                OUTPUT_DIR,
                f"{os.path.splitext(filename)[0]}_square_{square_num}.png"
            )

            cv2.imwrite(square_path, square)

            print(f"Saved square {square_num}")

            # draw rectangle for visual debug
            cv2.rectangle(
                debug,
                (x1, y1),
                (x2, y2),
                (0, 0, 255),
                4
            )

            # label square number
            cv2.putText(
                debug,
                str(square_num),
                (x1 + 20, y1 + 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                2,
                (255, 0, 0),
                4
            )

            square_num += 1

    # save debug image
    debug_path = os.path.join(
        DEBUG_DIR,
        f"debug_{filename}"
    )

    cv2.imwrite(debug_path, debug)

    print(f"Saved debug image: {debug_path}")


def main():

    files = sorted([
        f for f in os.listdir(INPUT_DIR)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ])

    if not files:
        print("No images found.")
        return

    for file in files:

        path = os.path.join(INPUT_DIR, file)

        process_image(path)

    print("\nDone.")


if __name__ == "__main__":
    main()