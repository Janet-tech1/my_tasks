# Python Operators
# Operators are special symbols in Python that perform operations on variables and values.

# 1. Comparison Operators**
# Comparison operators are used to compare two values. The result is always True or False, Yes or No, 0 or 1.

a = 10
b = 20

# Equal to  
print(a == b)                          # Output is False
# Not equal to 
print(a != b)                          # Output is True
# Greater than 
print(a > b)                           # Output is False
# Less than   
print(a < b)                           # Output is True
# Greater than or equal to 
print(a >= 10)                         # Output is True
# Less than or equal to 
print(b <= 25)                         # Output is True

# Use case Example- Student Exam Result
score = 75
print(score >= 50)        # True  (Passed)
print(score < 50)         # False (Failed)
print(score == 100)       # False (Not a perfect score)


# 2. Assignment Operators
# Assignment operators are used to assign values to variables. They can also combine an operation with assignment, so instead of writing x = x + 5, we can write x += 5.

x = 10
print("Initial value:", x)         # Output Initial value: 10

x += 5  # Equivalent to x = x + 5
# x += 5 means Adding 5 to x (x = x + 5) i.e 10 + 5 = 15
print("After += 5:", x)            # Output After +=5: 15

x -= 2         # x -= 2 means Subtracting 2 from x. i.e 15 - 2 = 13, since x is now 15
print("After x -=2:", x)

x *= 3         # x *= 3 means Multiplying x by 3. i.e 13 * 3 = 39
print("After x *= 3:", x)

x /= 4           # x /= 4 means Dividing x by 4. i.e 39/4 = 9.75
print("After x /= 4:", x)

x %= 3      # stores the remainder of x divided by 3. i.e 9.75 % 3 = 0.75
print("After x %= 3:", x)

x = 4
x **= 2       #  Raises x to the power of 2. i.e 4 ** 2 = 16
print("After x **= 2:", x)

x //= 3          # Floor divides x by 3. i.e 16 // 3 = 5 it does not include the decimal part or remainder
print("After x //= 3:", x)

# Use case Example:
# Define variables
balance = 1000
deposit = 200
withdraw = 150
balance += deposit   # Add deposit
balance -= withdraw  # Subtract withdrawal
print("Updated Balance:", balance)  
# Output: Updated Balance: 1050

# 3. Logical Operators
# Logical operators are used to combine conditional statements. They work with Boolean values (True or False).

x = 10
y = 20

# and operator  (True if both conditions are true )
print(x > 5 and y > 15)  # True

# or operator          (True if at least one condition is true)
print(x < 5 or y > 15)   # True

# not operator         (True if the condition is false )
print(not(x == 10))      # False

# Use case example1 - Scholarship Eligibility
# Define variables
age = 17
score = 85

# Must be younger than 18 AND score above 80
eligible = (age < 18) and (score > 80)
print("Scholarship Eligible:", eligible)  
# Output: Scholarship Eligible: True

# Use case example 2 - Event Access
age = 22
has_ticket = False
can_enter = (age >= 18) and (has_ticket or age < 25)
print("Access Granted:", can_enter)  
# Output: Access Granted: True (because age < 25 even without ticket)



