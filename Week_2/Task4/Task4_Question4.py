# Name Organiser
# Ask the User to Enter 5 names (separated by spaces)
text = input("Enter five names separated by spaces:")

# Convert all names to lowercase
print(text.lower())

# sort the list alphabetically
mylist = (text.lower())
mylist = mylist.split()
mylist.sort()
print(mylist)

# Display them one name per line.
for name in mylist:
 print(name)

