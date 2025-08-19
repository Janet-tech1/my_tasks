# The Federal Government of Nigeria has set the minimum age for admission into federal tertiary institutions at 16 years old for the 2025/2026 academic session, according to the Minister of Education, Dr. Tunji Alausa. This policy, announced at the 2025 JAMB policy meeting, replaces the previous 18-year minimum age requirement. 

# For the 2025/2026 academic session, the University of Lagos (UNILAG) requires candidates to have a minimum UTME score of 200 to be eligible for the Post-UTME screening. The Post-UTME itself is an online screening exercise. UNILAG does not release specific departmental cut-off marks before the screening. The departmental cut-off marks are determined after the Post-UTME, based on merit and the performance of candidates in both UTME and the Post-UTME. 


print("Welcome to UNILAG Admision Eligibility Checker Site for 2025/2026 Academic Session.")
print("\nKIndly input the following information to check your eligibility for the admission.")
name = input("Enter your full name (surname first): ")
age = int(input("Enter your age: "))
course = input("Enter your course of interest: ")
utme = int(input("Enter your Jamb score: "))
waec = input("Do you have at least five credits in your O'level result (including English and Mathematics): ")
first_choice = input("Did you choose UNILAG as your first choice: ")
post_utme = int(input("Enter your Post UTME score: "))
dept_cut_off = int(input("Enter your departmental cut-off mark (200-320): ")) 


eligibility = (age >= 16) and (utme >= 200) and (first_choice == "Yes") and (waec == "Yes") and (post_utme >= 50) and (dept_cut_off >= 200)

result = {True: "Congratulations, you meet all the requirements and have been offered admission", False: "Sorry, you do not meet the requirements for the admission"}


print(f"Candidate: {name}\nAge: {age}\nCourse of study: {course}\nUTME score: {utme}\nIs UNILAG your first choice: {first_choice}\nDo you have at least five credits in your O'level result: {waec}\nPost UTME score: {post_utme}\nDepartmental Cut-Off Mark: {dept_cut_off}")

print(f"\n\n\t\t\tADMISSION STATUS: \nDear {name}, {result[eligibility]} to study {course}.")






