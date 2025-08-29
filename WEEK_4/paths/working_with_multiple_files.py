# Working with multiple files at once- Sometimes you need to read from one file and write to another at the same time.
from pathlib import Path

workspace = Path("workspace_files")
input_file = workspace / "original.txt"
output_file = workspace / "processed.txt"

# Create an input file with some text
sample_text = """hello world
python programming
file handling tutorial
learning is fun"""

with open(input_file, "w", encoding="utf-8") as f:
    f.write(sample_text)

print("Created input file")

# Process the file: read from input, write processed version to output
with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", encoding="utf-8") as outfile:
    
    line_number = 1
    for line in infile:
        # Process each line: make it uppercase and add line numbers
        processed_line = f"Line {line_number}: {line.strip().upper()}\n"
        outfile.write(processed_line)
        line_number += 1

print("File processing complete!")

# Show the results
print("\nOriginal file:")
with open(input_file, "r", encoding="utf-8") as f:
    print(f.read())

print("\nProcessed file:")
with open(output_file, "r", encoding="utf-8") as f:
    print(f.read())

# Output to expect
"""
Created input file
File processing complete!

Original file:
hello world
python programming
file handling tutorial
learning is fun

Processed file:
Line 1: HELLO WORLD
Line 2: PYTHON PROGRAMMING
Line 3: FILE HANDLING TUTORIAL
Line 4: LEARNING IS FUN
"""