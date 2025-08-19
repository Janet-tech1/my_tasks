
# Eligibility Checker
print("Dear Candidate, please input the following info for the eligibility checker.")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your test score: "))

eligibility = (age < 18) and (score > 70)   # For the candidate to be eligible, he must be less than 18 years and his score must be greater than 70

print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

"""The code prints the candidate's information. e.g the name, age and score to know if they are eligible by scoring above 70 and less than 18 years of age.""" 


# Federal Government Scholarship Key Eligibility Requirements:

print("\nEnroll for the ongoing Federal Government Scholarship by answering the following questions with (Yes or No).")
citizenship = input("Are you a citizen of Nigeria: ")
enrollment = input("Are you a registered, full-time undergraduate student in a recognized Nigerian university: ")
other_scholarships = input("Are you currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international: ") 
qualification = input("Do you have at least five credits in your O'level result (Maths and English inclusive): ")

eligibility = (citizenship == "Yes") and (enrollment == "Yes") and(other_scholarships == "No") and (qualification == "Yes")

result = {True: "Congratulations, you are eligible for the 2025 ongoing Federal Government Scholarship.", False: "Sorry, you're not eligible for the ongoing Federal Government Scholarship."}

print(f"\nAre you a citizen of Nigeria: {citizenship}\nAre you a full time undergraduate: {enrollment}\nAre you a beneficiary of an existing scholarship: {other_scholarships}\nMinimum of five credits in O'level result: {qualification}\nEligible: {eligibility}")

print(result[eligibility])





