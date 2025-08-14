# Ask a user for their; first name, age, favorite colorand hometown
print("Hello dear friend! \nPlease enter the following details:")
name = input("First name:")
age = input("Age:")
color = input("Favorite colour:")
home_town = input("Home town:")

# Store them in a tuple profile and unpack into variables.
person = (name, age, color, home_town)
name,age,color,home_town = person
print(person)

# Print and use  escape sequence to align each piece of information nicely.
print("\nHere are the information required:")
print(f"My name is {name}.\nI am {age} years old.\nMy favorite color is {color}.\nI am from {home_town}.")
