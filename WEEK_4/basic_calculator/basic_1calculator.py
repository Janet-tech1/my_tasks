# """A basic calculator is one of the fundamentalprojects in Python programming. It provides essentialarithmetic operations such as addition, subtraction,multiplication, and division. Understanding how toimplement a calculator helps in learning user inputhandling, conditional statements, and function creation inPython.

# Key Concepts of Basic Calculator in Python
#  Arithmetic Operations:
#  Addition ( + )
#  Subtraction (- )
#  Multiplication ( * )
#  Division ( / )
#  Modulus ( % )
#  Exponentiation ( ** )
#  User Input Handling:
#  Using input() function
#  Converting strings to integers or floats
#  Functions in Python:
#  Defining functions for calculations
#  Calling functions with user inputs
#  Error Handling:
#  Parameter Table
#  Operator
#  Handling division by zero
#  Handling invalid inputs
#  """



# Simple Calculator Program
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

# Display operation options to the user
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take input from the user for operation choice
choice = input("Enter choice (1/2/3/4): ")     # from options 1-4

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
else:
    print("Invalid choice")






