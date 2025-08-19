# Store Inventory Update
# Create a dictionary called store with items and their available quantities. Example: store = {"Book": 10, "Pen": 20, "Bag": 5}
store = {}

# Available items
items = ["Microphone", "Keyboard", "Printer", "Monitor", "Mouse"]
# Quantity of each item
qty = [300, 450, 670, 250, 900]
print("The quantity of each available items are: ")
store = {items[0]: qty[0], items[1]: qty[1], items[2]: qty[2], items[3]: qty[3], items[4]: qty[4]}
print(store)
before_purchase = {item: quantity for item, quantity in store.items()}

# Ask the user to input the item they want to buy (e.g., "Pen").
purchase = input("\nEnter the item you want to buy from the store: ")

# Ask the user to input the quantity they want to purchase.
quantity = int(input("Enter the quantity of item you want to buy from the store: "))

# Use the assignment operator -= to update (reduce) the item quantity in the dictionary.
store[purchase] -= quantity         
print(store)

# Print the updated dictionary in this format:
# print(f"Before purchase: {store}\nAfter purchase: {after_purchase}")
print(f"\n\t\t\t=====Updated dictionarry=====\nBefore purchase: {before_purchase}\nAfter purchase: {store}")









