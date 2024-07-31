# Project name: Get Direcotry name and save to csv.
# By:           Chalongchaii@gmail.com
# 22-02-2023    Generate cript from ChatGPT.

import os
import csv

# Set the directory to read files from
directory = r"F:\Video"

# Set the output file name
output_file = "D:\GetFilename\output.csv"

# Initialize an empty list to store directory names
dir_names = []

# Walk through the directory tree
for root, dirs, files in os.walk(directory):
    for dir_name in dirs:
        if not dir_name.startswith('$') and dir_name not in ['.TemporaryItems', '.Trashes', '.DS_Store']:
            full_path = os.path.join(root, dir_name)
            dir_names.append(os.path.relpath(full_path, directory))

# Write the directory names to a CSV file
with open(output_file, "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Directory Name"])  # Write the header row
    for dir_name in dir_names:
        writer.writerow([dir_name])

print("Done.")
