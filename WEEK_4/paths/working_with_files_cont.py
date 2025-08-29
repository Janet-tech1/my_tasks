#**What Happens When Things Go Wrong?*- Sometimes files don't exist, or we don't have permission to read them. Python will give us an error, but we can catch and handle these errors gracefully. Let's see how to do that.
from pathlib import Path

workspace = Path("workspace_files")
workspace.mkdir(exist_ok=True)

# Try to read a file that doesn't exist
try:
    with open(workspace / "missing_file.txt", "r") as f:
        content = f.read()
        print("File content:", content)
except FileNotFoundError:
    print("Oops! That file doesn't exist yet.")
    print("Let's create it first!")
    
    # Now create the file
    with open(workspace / "missing_file.txt", "w") as f:
        f.write("Now I exist!")
    print("File created successfully!")


# If you write this correctly, you should see something like this...

"""
Oops! That file doesn't exist yet.
Let's create it first!
File created successfully!
"""


# **Checking If Files Exist Before Using Them*- Before trying to read or write files, it's smart to check if they exist first.
from pathlib import Path

workspace = Path("workspace_files")
file_path = workspace / "notes.txt"

# Check if our file exists
if file_path.exists():
    print(f"Found the file: {file_path.name}")
    
    # Get some information about the file
    file_size = file_path.stat().st_size
    print(f"File size: {file_size} bytes")
    
    # Read and show the content
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        print(f"Content preview: {content[:50]}...")  # First 50 characters
else:
    print(f"File {file_path.name} doesn't exist")
    print("You might want to create it first!")

# If notes.txt exists
"""
Found the file: notes.txt
File size: 67 bytes
Content preview: Todo:
 - Revise Python file handling
 - Practice J...

"""

# if notes.txt does not exist

"""
File notes.txt doesn't exist
You might want to create it first!
"""

















