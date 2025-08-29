# 1. Current Working Directory (CWD)
# This is how it works
# Using os.getcwd()
import os
# To get current working directory
print("Current working directory:", os.getcwd())


# 2. Absolute vs. Relative Paths
# Absolute path example
absolute_path = r"C:\/Users/user/Desktop/paths/my_path.py"
# Relative path example
relative_path = "my_path.py"

print("Absolute Path:", absolute_path)
print("Relative Path:", relative_path)


# 3. Joining Paths (The Right Way)
import os
folder = "C:/Users/user/Desktop/paths"
filename = "my_path.py"

path = os.path.join(folder, filename)
print("Full path:", path)

# This way, Python handles slashes (/ vs \) automatically.


# 4. Checking If a File or Folder Exists: We can check using `os.path.exists`

import os

path = "my_path.py"

if os.path.exists(path):
    print("Yes, the file exists!")
else:
    print("File not found.")


# 5. Using pathlib (Modern Way)- Python has a modern library called `pathlib`, which is easier to use than `os`.
from pathlib import Path

# Current working directory
print("Current directory:", Path.cwd())

# Create a Path object
file = Path("myfile.txt")

# Check if it exists
print("File exists:", file.exists())

# Combine paths
folder = Path("C:/Users/user/Desktop/paths")
full_path = folder / "myfile.txt"
print("Full path:", full_path)


# 6. Navigating Folders with pathlib
from pathlib import Path

# Get parent folder of current file
print("Parent folder:", Path.cwd().parent)

# List all files in a directory
for file in Path.cwd().iterdir():
    print(file)



