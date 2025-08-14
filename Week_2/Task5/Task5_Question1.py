# Ask the user to enter three favorite Nigerian dishes (one at a time).
print("Hello friend! Please provide the following details.")
text1 = input("Enter your first favorite dish:")
text2 = input("Enter your first favorite dish:")
text3 = input("Enter your first favorite dish:")

# Store them in a tuple called dishes.
dishes = (text1, text2, text3)
dishes_tuple = tuple(dishes) 
 
# Print the tuple in a single line, separating items with commas.
print("\nMy favorite dishes are:")
print(dishes_tuple) 

# Use the \n escape sequence to print each dish on a new line.
print("\nMy favorite dishes are:")
print(text1 +  "\n" + text2 + "\n" + text3) 


