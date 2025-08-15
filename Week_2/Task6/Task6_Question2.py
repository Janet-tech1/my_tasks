# Write a program that collects the names of people attending a seminar (no duplicates allowed) and displays them in alphabetical order.
print("Welcome to the AI Seminar, Please Input Your Name:")
visitors = set()

visitors.add(input("Enter your name: "))
visitors.add(input("Enter your name: "))
visitors.add(input("Enter your name: "))
visitors.add(input("Enter your name: "))
visitors.add(input("Enter your name: "))
visitors.add(input("Enter your name: "))   # The add command removes duplicate names automatically

# Duplicate, ignored automatically
print("Visitors:", visitors)   

# Displays the names in alphabetical order.
names = sorted(visitors)
print(f"Names of visitors: {names}")

