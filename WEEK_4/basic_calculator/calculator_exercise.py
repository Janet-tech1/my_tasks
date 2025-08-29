# **Hands-On Exercise**
# Try modifying the calculator with the following additional features:
# 1. Add a square root function that calculates the square root of a number.
# 2. Add an exponentiation function ( x^y ) thatraises one number to the power of another.
# 3. Allow the user to perform multiplecalculations without restarting the program.
# 4. Improve the user interface by formatting theoutput neatly.
# 5. Implement an option to exit the program when the user is done calculating


import math
# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract second number from first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide first number by second
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Function to calculate square root of a number
def sqrt(a):
    return math.sqrt(a)

# Function to calculate square root of a number
def sqrt(b):
    return math.sqrt(b)

# Function to raise one number to the power of another(exponential)
def add(a, b):
    return a**b


# Display operation options to the user
while True: 
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square root of number 1")
    print("6. Square root of number 2")
    print("7. Exponential")
    print("8. Exit")

# Take input from the user for operation choice
    choice = input("Enter choice: ")     # from options 1-4

# Get two numbers as input from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

# Perform calculation based on user's choice
    if choice == '1':
        print("Result:", add(num1, num2))

    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        print("Result:", math.sqrt(num1))    
    elif choice == '6':
        print("Result:", math.sqrt(num2))
    elif choice == '7':
        print("Result:", pow(num1, num2))
    elif choice == "8":
        print("Exited") 
        break
    else:
        print("Invalid choice")
