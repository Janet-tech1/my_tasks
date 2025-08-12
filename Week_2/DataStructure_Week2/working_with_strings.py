# Single quotes
name = 'Victoria'
print(f"My name is {name}. ")

# Double quotes
greeting = "Hello"
print(f"{greeting} Victoria! Tell me a story.")

# Triple quotes (for multi-line strings)
story = '''Once upon a time,
there was a coder named Victoria.
She lived in London,
and she has a very sweet personality.'''
print(f"{story}")

# Strings with numbers and symbols
password = "p@ssword123"
print(f"My password is: {password}")

# String Operations
# Indexing
word = "Welcome to Python!"
print(word[0])          # W
print(word[1])          # e
print(word[2])          # l
print(word[3])          # c
print(word[4])          # o
print(word[5])          # m
print(word[6])          # e
print(word[-1])         # !
print(word[-2])         # n

word = "rear"
print(word[0])           # r
print(word[1])           # e
print(word[2])           # a
print(word[3])           # r
print(word[-1])          # r
print(word[-2])          # a
print(word[-3])          # e
print(word[-4])          # r

# Slicing
word = "Python"
print(word[0:4])         # Pyth
print(word[2:])          # thon
print(word[2:5])
print(word[3:6])
print(word[:3])          # Pyt
print(word[::3])
print(word[::2])         # Pto
print(word[::-1])

# String Concatenation and Repetition
#Concatenation
a = "Hello"
b = "World!"
print(a + " " + b)        # Hello World
a = "Hello"
b = "Jane!"
c = "How"
d = "are"
e = "you?"
print(a + " " + b + " " + c + " " + d + " " + e)   

# Repetition
word = "Hi! "
print(word * 3)          # Hi!  Hi!  Hi!
word = "I Love Fried Rice! "
print(word * 3)

# String Searching and Checking

# Membership
text = "Python programming"
print("Python" in text)       # True
print("Java" not in text)     # True
print("Python" not in text)   # False
print("Java" in text)         # False

text =  "I miss you"
print("Love" in text)          # False
print("miss" in text)          # True
print("you" not in text)       # False
print("how" in text)           # False
print("you" in text)

# find() / rfind()
text = ("Hello World")
print(text.find("o"))         # 4
print(text.rfind("o"))        # 7

text = ("My name is Janet")
print(text.find("a"))         # 4
print(text.rfind("a"))        # 12

# index() / rindex()
text = "Hello World, You are Welcome"
print(text.index("World"))      # 6
print(text.index("Hello"))      # 0
print(text.index("You"))        # 13 
print(text.index("are"))        # 17
print(text.index("Welcome"))    # 21

# Startswith() / endswith()
filename = "data.csv"
print(filename.startswith("data"))       # True
print(filename.endswith(".csv"))         # True