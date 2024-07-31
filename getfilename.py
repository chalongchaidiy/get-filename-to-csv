# Project name: Get file name and save to csv.
# By:           Chalongchaii@gmail.com
# 22-02-2023    Generate cript from ChatGPT.

import os
import csv

# Set the directory to read files from
directory = r"F:\Video"

# Set the output file name
output_file = "D:\GetFilename\output.csv"

# Initialize an empty list to store file names
file_names = []

# Loop through the directory and its subdirectories and append file names to the list
for root, dirs, files in os.walk(directory):
    for file in files:
        if not file == ".DS_Store":
            if not file.endswith(".db"):  # Skip Thumbs.db               
                file_name = os.path.join(root, file)
                with open(file_name, "r", encoding="utf-8") as f:
                    # file_content = f.read()            
                    file_names.append(os.path.relpath(file_name, directory))
                
                print(file_names)
    # Write the file names to a CSV file
with open(output_file, "w", encoding="utf-8", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Directory Name", "File Name"])  # Write the header row
    for file_name in file_names:
        directory_name = os.path.basename(directory)
        writer.writerow([directory_name, file_name])
        
print(f"Done >> Save output file to {output_file}")