import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

picked_colors = []

def onclick(event, img_array):
    if event.xdata is None or event.ydata is None:
        return

    x = int(event.xdata)
    y = int(event.ydata)

    color = img_array[y, x]
    r, g, b = color

    print(f"Picked pixel at ({x}, {y}) -> RGB: ({r}, {g}, {b})")

    picked_colors.append((r, g, b))


def run_picker(image_path):
    img = Image.open(image_path).convert("RGB")
    img_array = np.array(img)

    fig, ax = plt.subplots()
    ax.imshow(img_array)
    ax.set_title("Click pixels to sample colors (close window when done)")

    fig.canvas.mpl_connect(
        "button_press_event",
        lambda event: onclick(event, img_array)
    )

    plt.show()

    print("\n--- FINAL PICKED COLORS ---")
    for c in picked_colors:
        print(c)


if __name__ == "__main__":
    run_picker("screenshots/screen2.png")