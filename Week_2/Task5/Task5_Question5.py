# Ask a user to enter three items for their shopping list.
shopping_list = []

print("Hello, Welcome to Sweetfingers Mall!")
print("\nPlease, list out the items you'd like to purchase.")

item1 = input("Enter the first item:")
item2 = input("Enter the second item:")
item3 = input("Enter the third item:")

# Store in a tuple shopping_list.
shopping_list = (item1, item2, item3)
print(shopping_list)

# Convert it to a list, then ask for two more items to add.
# Tuple to list
shopping_list = (item1, item2, item3)
lst = list(shopping_list)

print("\nPlease input two more items.")

lst.append(input("Enter the fourth item:"))
lst.append(input("Enter the fifth item:"))
print("\nThis is my shopping list")
print(lst)
 
# Convert back to a tuple and print the updated list using join() to display items separated by " | ".
shopping_list = tuple(lst)
print(shopping_list)  
print("\nHere's my shopping list:")
print(" | ".join(shopping_list))   