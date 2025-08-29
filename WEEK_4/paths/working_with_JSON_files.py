#**Working with JSON Files (Storing Data)**- JSON files are great for storing structured data like dictionaries and lists. Think of them as a way to save Python data to a file.

import json
from pathlib import Path

workspace = Path("workspace_files")

# Create some student data (like a mini database)
student_data = {
    "name": "Oyindamola",
    "age": 16,
    "courses": ["Python", "Data Science", "Web Development"],
    "grades": {"Python": "A", "Data Science": "B+", "Web Development": "A-"},
    "is_graduated": False
}

# Save the data to a JSON file
json_file = workspace / "student_data.json"
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(student_data, f, indent=2)  # indent=2 makes it pretty and readable

print("Student data saved to JSON file!")

# Now read it back
with open(json_file, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print("\nData read from JSON file:")
print(f"Student name: {loaded_data['name']}")
print(f"Age: {loaded_data['age']}")
print(f"Courses: {', '.join(loaded_data['courses'])}")
print(f"Python grade: {loaded_data['grades']['Python']}")