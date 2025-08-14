# Ask the user for 5 best friends’ names.
print("Hello, buddy!")
text1 = input("Enter the name of your first best friend:")
text2 = input("Enter the name of your second best friend:")
text3 = input("Enter the name of your third best friend:")
text4 = input("Enter the name of your fourth best friend:")
text5 = input("Enter the name of your fifth best friend:")

# Store them in a tuple friends.
print("\nThe names of my best friends are:")
friends = (text1, text2, text3, text4, text5)
friends_tuple = tuple(friends) 
print(friends)

# Print the tuple in reverse order.
print(friends[::-1])

