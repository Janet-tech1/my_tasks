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
name = input("Enter student's full name: ")
age = int(input("Enter student's age: "))
gender = input("Enter gender (Male/Female): ")
matric_num = int(input("Enter student matric number: "))
email = input("Enter student's email: ")

# Academic Scores (5 subjects)
subjects = ("Math", "English", "Economics", "Chemistry", "Biology")
scores = tuple(float(input(f"Enter score for {subj}: ")) for subj in subjects)

# Guardian Info
guardian_name = input("Enter guardian's name: ")
guardian_phone = input("Enter guardian's phone number: ")
guardian_address = input("Enter guardian's address: ")

# Hobbies - ensure uniqueness with set
hobbies = input("Enter at least 5 hobbies (comma-separated): ")
hobbies_set = set(h.strip() for h in hobbies.split(","))

# Student Dictionary
student_profile = {
    "Personal Details": {
        "Name": name.title(),
        "Age": age,
        "Gender": gender.capitalize(),
        "Matric_Number": matric_num,
        "Email": email.lower()
    },
    "Academics": {subj: score for subj, score in zip(subjects, scores)},
    "Guardian": {
        "Name": guardian_name.title(),
        "Phone": guardian_phone,
        "Address" : guardian_address
    },
    "Hobbies": list(hobbies_set)
}

# Derived Data
student_profile["Academics"]["Average"] = sum(scores) / len(scores)
student_profile["Personal Details"]["Initials"] = "".join([n[0] for n in name.split()])
student_profile["Hobbies Count"] = len(hobbies_set)

# Output Section
print("\n\t=== STUDENT PROFILE ===")
print(f"Name:\t\t{student_profile['Personal Details']['Name']}")
print(f"Age:\t\t{student_profile['Personal Details']['Age']}")
print(f"Gender:\t\t{student_profile['Personal Details']['Gender']}")
print(f"Initials:\t{student_profile['Personal Details']['Initials']}")
print(f"Matric_Number:\t{student_profile['Personal Details']['Matric_Number']}")
print(f"Email:\t\t{student_profile['Personal Details']['Email']}")

print("\n--- Academic Scores ---")
print(student_profile["Academics"])

print("\n--- Guardian Info ---")
print(student_profile["Guardian"])

print("\n--- Hobbies ---")
print(student_profile["Hobbies"])

print(f"\nTotal Hobbies:\t{student_profile['Hobbies Count']}")
print(f"Average Score:\t{student_profile['Academics']['Average']:.2f}")




















