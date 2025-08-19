
# Student Record
# Create an empty dictionary called student.
students = {}
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Ask the user to input their name and age, then store them in the dictionary.
student = {
    "Name": name,
    "Age": age,
}
print(student)

# Add a list of scores (e.g., [70, 85, 90]) to the dictionary.
scores = [70, 55, 80]
print(scores)

# Use a comparison operator to check if the student has passed (average score >= 50). Save the result (True/False) in the dictionary under the key "passed".
average_score = (70 + 55 + 80)/3   
print(average_score >= 50)   # True (passed)
passed = (average_score >= 50)

# Use a logical operator to check if the student is a teenager (age between 13 and 19). Save the result as "teenager".
teenager = (age > 12) and (age < 20)
print("Teenager:", teenager)   # Output: Teenager: True

# Print out the complete record 
print(f"\nStudent Record:\nName: {name} \nAge: {age}\nScores: {scores}\nPassed: {passed}\nTeenager: {teenager}")






