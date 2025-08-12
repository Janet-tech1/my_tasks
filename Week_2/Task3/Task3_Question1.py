# 1. Write a program to take a string input and display it in uppercase
first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
print(first_name.upper() + " " + last_name.upper())


# 2. Print first and last characters of the string
word = "python"
print(word[0::5])


# 3. Ask user for name and print, "Hello,!" where is the user's input
name = input("Enter your name:")
print(f"Hello! My name is {name}.")


# 4. Write a program to count the number of characters in a string without using len()
text = "Janet"
print(sum(1 for _ in text))


# 5. Given "Hello World", replace "World" with "Python"
text = "Hello World"
print(text.replace("World", "Python"))
