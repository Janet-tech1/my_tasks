# Tuple: is an ordered, immutable(unchangeable) collection of items in Python
# Creating Tuples

# 1. Using parentheses()
# Example 1: tuple with multiple items
fruits = ("apple", "banana", "cherry")
print(fruits)               # ('apple', 'banana', 'cherry')

# 2. Without parentheses (tuple packing)
numbers = 1, 2, 3
print(numbers)             # (1, 2, 3)

# 3. Single-item tuple (must include comma)
single_item = ("apple")
print(single_item)            #('apple')
print(type(single_item))      # <class 'tuple'>

# 4. Using the tuple() constructor
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)          #('apple', 'banana', 'cherry')

# Characteristics of tuple
# 1. Ordered
colors = ("red", "green", "blue")
print(colors[0])              # red

# # 2. Immutable (uncomment and run. This will cause an error)
colors = ("red", "yellow", "blue")
# colors[1] = "yellow"            # Type error
print(colors[1])

# 3. Allow duplicates
number = (1, 2, 2, 3)
print(numbers)              #(1, 2, 2, 3)

# 4. Mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed)                  # ("apple", 3, True, 5.6)

# 5. Nested Tuples
nested= (("a", "b"), (1, 2))
print(nested)               # (('a', 'b'), (1, 2))

# Tuple Opertaions
# 1. Indexing
fruits = ("apple", "banana", "cherry")
print(fruits[1])             # banana
print(fruits[-1])            # Cherry

# 2. Slicing
print(fruits[0:2])             # ('apple', 'banana')
print (fruits[::-1])           # ('cherry', 'banana', 'apple')

# 3. Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)                 # (1, 2, 3, 4)

# 4. Repetition
nums = (1, 2)
print(nums * 3)               # (1, 2, 1, 2, 1, 2)

# 5. Membership
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)          # True
print("grape" not in fruits)       # True

# 6. Iteration
for fruit in fruits:
    print(fruit)

# Unpacking Tuples
person = ("John", 25, "Nigeria")
name,age,country = person
print(name)              # John
print(age)               # 25
print(country)           # Nigeria

# Tuple methods: Tuples have only two methods
# dont count() and dot index()
numbers = (1, 2, 2, 3, 4, 5)
print(numbers.count(2))          # 2 (counts occurences of 2)
print(numbers.index(3))          # 3 (position of first occurence of 3)

# Converting Between List and Tuple
# Tuple to list
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst)                     # [1, 2, 3, 4]

# List back to tuple
t = tuple(lst)
print(t)                       # (1, 2, 3, 4)

# Built-in Functions with Tuples
nums = (4, 1, 7, 3)
print(len(nums))           # 4
print(max(nums))           # 7
print(min(nums))           # 1
print(sum(nums))           # 15

