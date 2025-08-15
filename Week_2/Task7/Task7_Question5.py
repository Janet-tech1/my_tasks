# Contact Quick Lookup**
# Requirements:
# Use `zip()` and d`ict()` to combine tuples.
# Use `.get()` for safe retrieval.
# No loops.


# Store three names and their phone numbers in two separate tuples.
names = ()
phone_num = ()

print("Input three names and their phone numbers for a quick contact lookup.")
names = ("Bisola", "Olamide", "Bolu")
print(f"The names are: {names}")

phone_num = ("07034567832", "08023456789", "09098765432")
print(f"The phone numbers are: {phone_num}")

# Create a dictionary from them using `dict(zip(...))`.
# Use `zip()` and d`ict()` to combine tuples.
print("\nThe names and phone numbers are:")
contact = dict(zip(names, phone_num))
print(contact)

# Ask the user for a name and display the corresponding number (or an error message).
# Use `.get()` for safe retrieval.
#get() function is used to retrieve the value associated witha specific key
print(contact.get(input("\nenter a name:"),"an error message"))




# NOTE
# dict(zip(..., ...)) are two iterables: one for key and one for values.
# the zip() fxn pairs corresponding elements from these iterables. 
# dict() converts these pairs into a dictionary
# zip(keys, values). e.g ("name, "Alice"), ("age", 30), and ("city", "New York")
# output will be: {"name: "Alice", "age": 30, "city": "New York"}







