# Unique Members Registration**
# Requirements:
# Use `.split(",")` and `set()` to remove duplicates.
# Use dictionary comprehension `{name: len(name) for name in set_of_names}`.



# Ask the user to enter three names separated by commas.
print("Input 3 names separated by commas")
names = input("The names separated by comma are: ")

# Convert them to a set to ensure uniqueness.
name = ()
names_set = set(n.strip() for n  in names.split(","))
print(names_set)

# Create a dictionary where each name is a key and its length is the value.
print("\nThe names and their length are:")
print({name: len(name) for name in names_set})




















