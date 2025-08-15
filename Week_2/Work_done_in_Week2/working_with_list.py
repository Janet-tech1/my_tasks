# Method 1: Using square brackets
empty_list = []
print(empty_list)                        # Output: []

text = ["My name is Jane"]               # Output: ['My name is Jane']
print(text)    

# Method 2: Using the list() constructor
empty_list2 = list()
print(empty_list2)                       # Output: []

text = list("My name is Janet")
print(text)    

# List of integers
numbers = [1, 2, 3, 4, 5]
print(numbers)                           # Output: [1, 2, 3, 4, 5]

numbers = [25, 30, 35, 40, 45, 50]
print(numbers)                           # Output: [25, 30, 35, 40, 45, 50]

# List of strings
fruits = ["apple", "banana", "cherry"]
print(fruits)                             # Output: ['apple', 'banana', 'cherry']
fruits = ['apple', 'banana', 'cherry']
print(fruits)

# Mixed data types
mixed_list = ["Alice", 25, 5.8, True]
print(mixed_list)                        # Output: ['Alice', 25, 5.8, True]
mixed_list = ["It is true that Afeez got", 76.5 ,"in his mathematics exam"]
print(mixed_list)                        # Output: ['It is true that Afeez got", 76.5 ,"in his mathematics exam']

# From a string (each character becaomes an element)
chars = list("hello")
print(chars)                             # Output: ['h', 'e', 'l', 'l', 'o']

# From a Tuple
my_tuple = (10, 20, 30 ,40 ,50)
list_from_tuple = list(my_tuple)
print(list_from_tuple)                  # Output: [10, 20, 30, 40, 50]

# From a range
numbers_range = list(range(5))
print(numbers_range)                    # Output: [0, 1, 2, 3, 4]

# Squares of numbers 0-4
squares = [x**2 for x in range(5)]
print(squares)                          # Output: [0, 1, 4, 9, 16]
squares = [x**2 for x in range(10)]
print(squares)                          # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
squares = [x**3 for x in range(4)]
print(squares)                          # Output: [0, 1, 8, 27]

# Even numbers between 0-10
evens = [x for x in range(11) if x % 2 == 0]
print(evens)                            # Output: {0, 2, 4, 6, 8, 10}
num = [x for x in range(11) if x % 3 == 0]
print(num)                              # Output: [0, 3, 6, 9]

# Creating a nested list. A list can contain other lists. It is useful for matrices or grouped data
# Matrix-like list
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix)                          # Output: [[1, 2], [3, 4], [5, 6]]

# Accessing elements in a nested list
print(matrix[0])                       # Output: [1, 2]
print(matrix[0][1])                    # Output: 2
print(matrix[1])                       # Output: [3, 4]
print(matrix[2])                       # Output: [5.6]


# Characteristics of a list
# Ordered collection
fruits = ["mango", "orange", "banana"]
print(fruits)                         # Output: ['mango', 'orange', 'banana']
print(fruits[0])                      # Output: mango
print(fruits[2])                      # Output: banana
print(fruits[1])                      # Output: orange

# Allows duplicates
items = ["rice", "beans", "yam", "rice"]
print(items)                          # Output: ['rice', 'beans', 'yam', 'rice']

# Mutable (can be changed)
numbers = [1, 2, 3]
numbers[1] = 20                       # Changing element at index 1
print(numbers)                        #[1, 20, 3]

numbers = [4, 5, 7, 9]
numbers[3] = 90                  # Changing element at index 3 from 9 to 90
print(numbers)                   # Output: [4, 5, 7, 90]

# Can contain different data types
mixed = [10, "Nigeria", 3.14, True]
print(mixed)                     # Output: [10, 'Nigeria', 3.14, True]

# Can be Nested
nested_list = [[1, 2], ["a", "b"]]
print(nested_list)                  # Output: [[1,2], ['a, 'b']]
print(nested_list[0][1])            # Output: 2

# Dynamic size
names = ["Ada"]
names.append("Bola")
names.append("Chidi")
print(names)                       #['Ada', 'Bola', 'Chidi']

