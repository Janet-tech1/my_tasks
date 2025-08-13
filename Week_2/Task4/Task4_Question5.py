# Student Score Tracker
names = []
scores = []
print(names)
print(scores)

# Ask the user for 3 student names and their scores
print("Hello welcome to student score tracker.")
name1 = input("Enter name of the first student:")
score1 = float(input("Enter score of the first student:"))
name2 = input("Enter name of the second student:")
score2 = float(input("Enter score of the second student:"))
name3 = input("Enter name of the third student:")
score3 = float(input("Enter score of the third student:"))

# Store the results in two lists (one for names, one for scores)
name = [name1, name2, name3]
score = [score1, score2, score3]

# Print a formatted output showing Name — Score, aligned neatly.
print("\nNames - Scores")
print(f"{name1} - {score1}")
print(f"{name2} - {score2}")
print(f"{name3} - {score3}")


