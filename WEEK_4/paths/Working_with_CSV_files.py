#**Working with CSV Files -Spreadsheet like Data**
# CSV files are like simple spreadsheets. They are perfect for storing data in rows and columns.

import csv
from pathlib import Path

workspace = Path("workspace_files")
csv_file = workspace / "students.csv"

# Create sample student data
students = [
    ["Name", "Age", "Course", "Grade"],  # Header row
    ["Precious", 20, "Python", "A"],
    ["Favour", 22, "JavaScript", "B+"],
    ["Ore", 21, "Python", "A-"],
    ["Susan", 23, "Data Science", "A"]
]

# Write data to CSV file
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(students)  # Write all rows at once

print("Student data written to CSV file!")

# Read the CSV file back
print("\nReading CSV file:")
with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    
    for row_number, row in enumerate(reader):
        if row_number == 0:  # Header row
            print(f"Headers: {' | '.join(row)}")
            print("-" * 40)
        else:  # Data rows
            name, age, course, grade = row
            print(f"{name} ({age} years) - {course}: {grade}")











