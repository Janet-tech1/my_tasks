# List Methods
# 1. dot append( method): Adds an element to the end of the list
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)              # Output: ['apple', 'banana', 'cherry']

# 2. dot insert() method: Inserts an element at a specific position
fruits = ["apple", "banana"]
fruits.insert(1, "orange")
print(fruits)             # Output: ['apple', 'orange', 'banana']

# 3. dot extend() method: Add elements from another list (or iterable) to the end
fruits = ["apple", "banana"]
tropical = ["mango", "pineapple"]
fruits.extend(tropical)
print(fruits)             # Output: ['apple', 'banana', 'mango', 'pineapple']

# 4. dot remove() method: Removes the first occurence of a specified value
fruits = ["apple", "banana", "mango", "pineapple"]
fruits.remove("banana")
print(fruits)           # Output: ['apple', 'mango', 'pineapple']

# 5. dot pop() method: Removes and returns the element at a givenindex (default: last)
fruits = ["apple", "banana", "cherry"]
last_fruit = fruits.pop()
print(last_fruit)          # Output: cherry
print(fruits)              # Output: ['apple', 'banana']

# 6. dot clear() method: Removes all elements from a list
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)                # Output: []

# 7. dot index() method: Returns the index of the first occurence of a value
fruits = ["apple", "banana", "cherry"]
position = fruits.index("banana")
print(position)                # Output: 1

# 8. dot count() method: Counts how many times a value appears
fruits = ["apple", "banana", "cherry", "banana"]
print(fruits.count("banana"))          # Output: 2

# 9. dot sort() method: Sorts the list in ascending order (default)
# ascending order
numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)             # Output: [1, 2, 3, 4]

# descending order
numbers.sort(reverse=True)
print(numbers)             # Output: [4, 3, 2, 1]

# 10. dot reverse() method: Reverses the order of a list
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(fruits)           # Output: ['cherry', 'banana', 'apple']

# 11. copy(): Returns a shallow copy of the list
fruits = ["apple", "banana", "cherry"]
new_list = fruits.copy()
print(new_list)              # Output: ['apple', 'banana', 'cherry']