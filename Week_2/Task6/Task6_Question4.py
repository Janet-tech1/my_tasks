# Ask for voter names and store in a set.
print("Welcome to voters registration center; please input your names")
voters = set()
voter1 = input("Name1: ")
voter2 = input("Name2: ")
voter3 = input("Name3: ")
voter4 = input("Name4: ")
voter5 = input("Name5: ")
voter6 = input("Name6: ")

# voters = (voter1, voter2, voter3, voter4, voter5, voter6)
# If a voter tries to register twice, display a warning.
for voter in [voter1, voter2, voter3, voter4, voter5, voter6]:
    if voter in voters:
        print(f"warning: {voter} has already registered!")     # warning signal
    else:
        voters.add(voter)

# After registration, display the total number of unique voters.
print("\nThe total number of unique voters are: ", len(voters))
print("Voters:", ", ". join(voters))


