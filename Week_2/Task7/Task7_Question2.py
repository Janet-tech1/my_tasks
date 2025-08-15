# Super Market Price List**
# Requirements:
# Use dictionary update method `.update()` or assignment.
# Use `.keys()` to display available items.
# Use input validation (no advanced functions).


# Create a program that stores items and their prices in a dictionary.
items = {}

# Items should come from a list.
print("The available items are:")
item1 = ("Malt")
item2 = ("Milo")
item3 = ("Milk")
item4 = ("Meat pie")
item5 = ("Macaroni")
items = (item1, item2, item3, item4, item5)
for key in items:
    print(key)

# Prices are entered by the user.
prices_list = {}

print("\nPlease input the prices of the items you want to purchase.")
price1= float(input("Enter price of malt: #"))
price2 = float(input("Enter price of milo: #"))
price3 = float(input("Enter price of milk: #"))
price4 = float(input("Enter price of meat pie: #"))
price5 = float(input("Enter price of macaroni: #"))
price_list = {price1, price2, price3, price4, price5}

# Display all items and prices, then allow the user to update the price of an item.
print(f"\nAvailable Items and their prices:\n{item1}: #{price1}\n{item2}: #{price2}\n{item3}: #{price3}\n{item4}: #{price4}\n{item5}: #{price5}\n")

# use .update() to update/change the price of an item
price_to_update = float(input("Enter the new price of Malt: #"))
price_list.update({price_to_update,})
price1 = price_to_update

# Print the new price
print(f"The new price of malk is: #{price_to_update}")
print("\nThe new price list for each items are:")
print(f"{item1}: #{price_to_update}\n{item2}: #{price2}\n{item3}: #{price3}\n{item4}: #{price4}\n{item5}: #{price5}\n")



