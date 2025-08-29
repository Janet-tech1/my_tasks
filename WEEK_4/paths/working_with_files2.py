# Setting up- its cleaner to work inside a folder so files dont clutter your desktop

from pathlib import Path

workspace = Path("workspace_files")
workspace.mkdir(exist_ok=True)
file_path = workspace / "notes.txt"
file_path

# 2. Create a file- There are two common ways to “create”:

# `w` (write): creates the file if it doesn’t exist; overwrites if it does.

# `x` (exclusive create): creates the file only if it doesn’t exist; errors if it does (safer if you don’t want to overwrite by mistake).

# Use `w` when you’re okay with replacing old content; use `x` when you want to avoid accidental overwrites.

 # (A) Create or overwrite using 'w'
f = open(file_path, "w", encoding="utf-8")
f.write("This is the first line in notes.txt\n")
f.close()

# (B) Safe-create using 'x' (uncomment to try once)
# f = open(workspace / "created_once.txt", "x", encoding="utf-8")
# f.write("This file will only be created if it doesn't exist.\n")
# f.close()

#3. Open a file- Opening a file prepares it for reading or writing.
# Open for writing again (this will overwrite!)
f = open(file_path, "w", encoding="utf-8")
f.write("Replaced the old content with this line.\n")
f.close()

# 4. Write to a file- Writing puts text into the file. write() does not add newlines automatically (you add `\n` yourself).
# Note: If you only want to add new content, don’t use 'w' — use 'a' (append).

f = open(file_path, "w", encoding="utf-8")
f.write("Shopping List:\n")
f.write(" - Rice\n")
f.write(" - Beans\n")
f.write(" - Garri\n")
f.close()

# 5. Append to a file- Append adds to the end without deleting whats already there.
f = open(file_path, "a", encoding="utf-8")
f.write(" - Groundnut oil\n")
f.write(" - Maggi\n")
f.write(" - Tomato\n")
f.write(" - Fish\n")
f.close()

# 6. Read from a file- There are four common ways:
# a. read()- whole file in one string
# b. read(n)- First n characters
# c. readline()- One line
# d. readlines()- List of all lines

# Read the whole file
f = open(file_path, "r", encoding="utf-8")
content = f.read()
f.close()
print(content) # this will bring out all the shopping lists

# Read line-by-line
f = open(file_path, "r", encoding="utf-8")
print("First line:", f.readline().rstrip())
print("Second line:", f.readline().rstrip())
f.close()   # This will print out only the first and second line

# Read as a list of lines
f = open(file_path, "r", encoding="utf-8")
lines = f.readlines()
f.close()
print("Lines list:", [line.rstrip() for line in lines]) # This will bring out the shopping list in a single line

# Iterate over lines (memory-friendly)
f = open(file_path, "r", encoding="utf-8")
for line in f:
    print("->", line.rstrip())
f.close()


# 7. Close the file- a. Always close files opened with open(...).
# b. It flushes (saves) any buffered data to disk.
# c.  It releases the OS handle so other programs can use the file.
# d. It avoids weird bugs (especially on Windows).
# You have seen f.close() above. But there’s a better way…


# 8. Use with open(...) as f: - The with statement automatically closes the file even if an error happens.
# Write safely
with open(file_path, "w", encoding="utf-8") as f:
    f.write("My Todo List:\n")
    f.write(" - Revise Python file handling\n")
    f.write(" - Practice error handling within a function")
    f.write(" - Practice JSON & CSV\n")

# Append safely
with open(file_path, "a", encoding="utf-8") as f:
    f.write(" - Build a small project\n")
    f.write(" - P   ass my exam\n")







