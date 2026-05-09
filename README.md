# Be Fish Data

## Introduction

This is a project I have been working on for a small game called be fish. In this project I collect data from screenshots using OCR and templates, process data using dictionaries and objects, and create automatic hotkey scripts.

For use I recommend to split the folders up for use of a virtual environment and library installation

## Data Collection

### User Guide

Create a virtual environment(Depends on what terminal you are running) and install required libraries with install statement below. Then add screenshots to screenshots folder in the same way as the example screenshots. Take screenshots using windows + shift + s and take a picture of a 4x2 area making sure not to repeat fish. Then run main.py and your data will be in data/data.txt

'''
pip install numpy pillow opencv-python pytesseract
'''

### Code Guide

The **main.py** runs all of the files other files one at a time exectuing the program properly.

The file exectution order is as follows
1. **black_white_filter.py** - filters images to only show important information in black with a white background
2. **make_squares.py** - splits 4x2 image into 8 squares each containing a fish name and number
3. **split_fish_number.py** - splits the fish and numbers into seperate images for better readability
4. **OCR_Fish.py** - Reads fish images with simple OCR reader and writes the names to a txt file
5. **template_comparer.py** - Compares templates in template folder to actual numbers to produce accurate results
6. **data_processor.py** - Combines number and fish name files
7. **rarity_calculator.py** - Reads bottom up calculating proper rarities based on number of occurences
8. **add_1.py** - adds 1 to each becauese the game stores improperly
9. **add_extra.py** - adds extra fish not yet unlocked as zeros

## Data Processing

### User Guide

Copy data from data.txt and paste into complete_data.txt. Run main.py and choose file input type. Choose from options.

### Code Guide

Programs Execution Order
1. **fish.py** - Creates Fish object with multiple variables
2. **Fetch.py** - Fetches data from json file preloaded with data for first run and loads into dictionary
3. **storage.py** - contains update function that updates with each change to the dictionary
4. **process.py** - Contains all important functions for data processing
5. **main.py** - contains questions for choice of data formating

## Hotkeys

Contains Two Hotkeys - Double click on file in file explorer to run

### Sweeper

Sweeps through field effectienctly with compressed speed input from be fish wiki. May need to adjust the scale factor. Over time the performance of code worsens as windows decreaeses sleep time so after a few hours of running increase scale factor. This is best for private servers

### Auto Farm

This is a simple hotkey that every few minutes turns on and off auto farm and holds w to avoid roblox and be fish auto rejon servers.

## Processing functions

1. **Display** - Simply displays each fish with amounts
2. **Total** - calculates and returns total fish
3. **fish_bulled** - calculates the total number of a fish species pulled from all rarities
4. **fish_pulled_stats** - returns a vector of all fish species amounts
5. **projected_amount** - returns the projected amount of fish required to pull a fish based of previous data
6. **projected_amount_list** - returns sorted list of projected amounts of fish required to get
7. **effecienct_list** - returns a list of fish to use in order
8. **best_fish** - returns best fish
9. **rarity_breakdown** - returns percentage of fish are each rarities (important for checking luck)

