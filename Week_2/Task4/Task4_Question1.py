# Your Favorite Life Quote

# Ask the user to input their favorite quote.
print("Hello Janet!")
sentence1 = input("Please, input your favorite quote:")    # Ask the User to Input Their favorite Quote
print("sentence1")

# Convert it to title case.
print(sentence1.title())             # Convert to title case 

sentence2 = input("Please, enter another quote:")         # Ask the User to Input Another Quote
print("sentence2")

print(sentence2.title())              # Convert to title case       

# Print it with quotation marks using escape sequences
print("Quote 1 and 2: " + sentence1.title() +  "\t" + sentence2.title() + "\n")  # Print it with quotation marks using escape sequence(\n and \t)
 
    