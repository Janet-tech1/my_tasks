# Student Bio-Data Storage
# Requirements:
# Use `input()` to collect details.
# Use dictionary operations `(dict[key] = value)` to store data.
# Use `print()` formatting with `\n` and `\t` for better output.


# Create a program that collects student bio-data from user input (name, age, gender, courses) and stores it in a dictionary.
bio_data = {}

print("Please input the following information for the student biodata storage.")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")
courses = input("Enter all your courses (comma separated): ") 

# Courses should be stored as a list.
course = []
course = [courses]
print(f"The courses are: {course}")


# Storing a student's biodata Using dictionary operations (dict[key] = value) 
print("\nMethod 1: Printing the output using the (dictionary[key] = value")
bio_data = {"name": name, "age": age, "gender": gender, "courses": course}
for key, value in bio_data.items():
    print(f"{key}: {value}")


# Display the bio-data neatly using escape sequences.
print("\nMethod 2: Printing the output in a portrait mode")
print(f"name:\t{name}\nage:\t{age}\ngender:\t{gender}\ncourses: {course}")


# It can also be presented this way
print("\nMethod 3: Printing the output in a landscape mode")
print("\nStudent Bio Data" )
print(f"Name\t\tAge\t\tGender\t\tCourses\n{name}\t\t{age}\t\t{gender}\t\t{course}")
