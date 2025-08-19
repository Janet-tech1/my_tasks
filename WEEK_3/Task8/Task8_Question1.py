
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# 1. Explain each output of the program below.
num1 = 20
num2 = 25
print(f"{num1} == {num2} : {num1 == num2}")  # Output: 20 == 25 :False    
# Explanation: 20 is not equal to 25 so the output is False

print(f"{num1} != {num2} : {num1 != num2}")    # Output: 20 != 25 : True
# Explanation: 20 is not equal to 25 so the output is True

print(f"{num1} > {num2} : {num1 > num2}")      # Output: 20 > 25 : False
# Explanation: 20 is not greater than 25 so the output is False

print(f"{num1} < {num2} : {num1 < num2}")      # Output: 20 < 25 : True
# Explanation: 20 is less than 25 so the output is True


# 2. Give 3 usecases or scenarios where you can apply the program below.
# a. Age verification
# b. Exam scoring
# c. Checking eligibility

# 3. Write the code for 1 of the 3 use cases.
# Age Verification
age = int(input("\nEnter your age: "))
if age > 17:
    print("Access granted.")
else:
    print("Access denied.")


 





