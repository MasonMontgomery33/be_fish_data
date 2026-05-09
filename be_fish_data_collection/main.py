import os
import subprocess
import sys

SRC_DIR = "src"

PIPELINE = [
    "black_white_filter.py",
    "make_squares.py",
    "split_fish_number.py",
    "OCR_Fish.py",
    "template_comparer.py",
    "data_processor.py",
    "rarity_calculator.py",
    "add_1.py",
    "add_extra.py"
]


def run_script(script_name):

    script_path = os.path.join(SRC_DIR, script_name)

    if not os.path.exists(script_path):
        print(f"\nERROR: Missing script: {script_path}")
        sys.exit(1)

    print("\n==============================")
    print(f"RUNNING: {script_name}")
    print("==============================")

    result = subprocess.run(
        [sys.executable, script_path]
    )

    if result.returncode != 0:
        print(f"\nERROR: {script_name} failed.")
        sys.exit(result.returncode)

    print(f"\nDONE: {script_name}")


def main():

    for script in PIPELINE:
        run_script(script)

    print("\n==============================")
    print("FULL PIPELINE COMPLETE")
    print("==============================")


if __name__ == "__main__":
    main()