# Moving around inside a file- Sometimes you want to jump to a specific part of a file instead of reading from the beginning.

from pathlib import Path

workspace = Path("workspace_files")
file_path = workspace / "story.txt"

# Create a sample story file
story = """Once upon a time, there was a lady  who was very curious and inquisitive, 
she just want to know how things work behind the scene. 
Eventually she had an opportunity to hop into the world of programming for the first time.
She started with python, now she codes in Python every day.
One day, she discovered file handling.
It opened up a whole new world of possibilities!
The end."""

with open(file_path, "w", encoding="utf-8") as f:
    f.write(story)

print("Created a story file!")

# Now let's explore moving around in the file
with open(file_path, "r", encoding="utf-8") as f:
    print("\nFile positioning demo:")
    
    # Read first 16 characters
    first_part = f.read(16)
    print(f"First 16 characters: '{first_part}'")
    
    # Check where we are now
    current_position = f.tell()
    print(f"Current position in file: {current_position}")
    
    # Jump to the beginning
    f.seek(0)
    print(f"After seeking to beginning: position {f.tell()}")
    
    # Jump to position 50 and read from there
    f.seek(49)
    rest_of_line = f.readline()
    print(f"Reading from position 49: '{rest_of_line.strip()}'")
    
    # Go back to beginning and read the first line
    f.seek(0)
    first_line = f.readline()
    print(f"First line: '{first_line.strip()}'")

    # Go to the second line and read the second line
    f.seek(0)
    story = f.read()
    print(f"Story: '{story.strip()}'")






