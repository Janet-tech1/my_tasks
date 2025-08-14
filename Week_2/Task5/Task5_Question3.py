# Create a tuple of 5 Nigerian states entered by the user.
print("Hello dear, please input 5 Nigerian states:")
state1 = input("Enter the first state:")
state2 = input("Enter the second state:")
state3 = input("Enter the third state:")
state4 = input("Enter the fourth state:")
state5 = input("Enter the fifth state:")
states = (state1, state2, state3, state4, state5) 
print(states)

# Print the first state and last state.
print("\nThe first and last state are:")
print(states[0::4])

# Check if "Lagos" is in the tuple and print "Yes" or "No".
print("\nIs Lagos in the states listed?")
if ("Lagos" in states):
    print("Yes")
elif ("Lagos" not in states):
    print("No")

# Print the number of states entered. (Hint: use the tuple membership)
print("\nWhat is the total number of states listed?")
print(len(states))