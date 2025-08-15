# Student Profile Builder**
# This program collects student details, academic scores, hobbies, and guardian info, stores them in a nested dictionary, and performs automatic calculations and transformations using dictionary comprehension, tuple unpacking, and set operations.

# I want to create a program that collects student information and presents it in a clean, organized way.
# The program should:
# Collect personal details (name, age, gender).
# Collect academic scores for a fixed set of subjects.
# Store guardian information.
# Store hobbies without duplicates.
# Automatically calculate average score and initials.


# Personal Details
print("Hello dear student, please fill in the details below for the student profile builder")
student_name = input("Enter student's full name: ")
student_age = int(input("Enter student's age: "))
student_gender = input("Enter gender (Male/Female): ")
student_matric_num = int(input("Enter student matric number: "))
student_email = input("Enter student's email: ")

# Academic Scores (5 Subjects)
print("\nFill in the subjects taken and their scores")
subjects = ("Maths", "English", "Economics", "Biology", "French")
scores = tuple(float(input(f"Enter score for {subject}, ")) for subject in subjects)

# Guardian Infomation
print("\nFill in the information of the student's guardian")
guardian_name = input("Enter guardian's name: ")
guardian_phone = int(input("Enter guardian's phone number: "))
guardian_address = input("Enter guardian's address: ")

# Hobbies
print("\nFill in the student's hobbies")
hobbies = ()
hobbies = input("Enter at least 4 hobbies (comma separated): ")
hobbies_set = set(h.strip() for h in hobbies.split(","))
print(hobbies_set)

# Student Dictionary
student_profile = {
    "Personal Details": {
       "Name": student_name.title(),
       "Age": student_age,
       "Gender": student_gender.capitalize(),
       "Matric Number": student_matric_num,
       "Email": student_email.lower()
    },
# Using zip(key, value)
    "Academics": {subject: score for subject, score in zip(subjects, scores)},
    "Guardian": {
        "Name": guardian_name.title(),
        "Phone number": guardian_phone,
        "Address": guardian_address
},
    "Hobbies": list(hobbies_set)
}

# Data Collected
student_profile["Academics"]["Average"] = sum(scores) / len(scores)
student_profile ["Personal Details"]["Initials"] = "".join([n[0] for n in student_name.split()])
student_profile["Hobbies Count"] = len(hobbies_set)

# Output Section
print("\n\t=== STUDENT PROFILE ===")
print(f"Name:\t\t{student_profile['Basic Info']['Name']}")
print(f"Age:\t\t{student_profile['Basic Info']['Age']}")
print(f"Gender:\t\t{student_profile['Basic Info']['Gender']}")
print(f"Initials:\t{student_profile['Basic Info']['Initials']}")

print("\n--- Academic Scores ---")
print(student_profile["Academics"])

print("\n--- Guardian Infomation ---")
print(student_profile["Guardian"])

print("\n--- Hobbies ---")
print(student_profile["Hobbies"])

print(f"\nTotal Hobbies:\t{student_profile['Hobbies Count']}")
print(f"Average Score:\t{student_profile['Academics']['Average']:.2f}")
























