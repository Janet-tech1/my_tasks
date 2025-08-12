# Creating and Manipulating Strings

# upper() (Convert all charaters in string to uppercase)
name = "Alex Iwobi" 
print(name.upper())                         # uppercase()


# lower() (Convert all charaters in string to Lowercase)
sentence = "python is amazing"
print(sentence.lower())                     # lowercase()


# title() (Converts all the first letter to uppercase)
sentence = "python is wonderful"
print(sentence.title())                     # title()


# capitalize() (Capitalize the first letter of the first word)
sentence = "python is wonderful"
print(sentence.capitalize())                # capitalize()


# strip() (Removes whitespace (or specified characters) from both ends of the string)
text = "   Abuja   "
print(text.strip())                         # strip()


# replace() (Replaces occurences of a substring with another substring )
message = "I love Java"
print(message.replace("Java", "Python"))    # replace()


# swapcase() (Switches lowercase to uppercase and vice versa)
text = "Hello ABEOKUTA"
print(text.swapcase())                      # swapcase()


# lstrip() (Removes whitespace(or specified characters) from the left side only)
text = "   Nigeria"
print(text.lstrip())                        # lstrip()


# rstrip() (Removes whitespace(or specified characters) from the right side only)
text = "Nigeria   "
print(text.rstrip())                        # rstrip()


# split() (Splits a string into a list using a separator (default is space)
fruits = "mango orange banana"
print(fruits.split())                       # split()


# rsplit() (Splits a string into a list from the right side)
text = "one,two,three,four"
print(text.rsplit(",", 2))                  # rsplit()


# splitlines() (Splits a string into a list at each newline(\n)
lines = "Line 1\nLine 2\nLine 3"
print(lines.splitlines())                   # splitlines()


# join() (Joins a list of strings into one string with a specified separator)
words = ["I", "love", "Python"]
print(" ".join(words))                      # join()


# center() (Centers the string within a specified width, padding with spaces or characters)
text = ("Python")
print(text.center(20, "-"))                 # center()


# ljust() (Left-aligns the string within a specified width, padding with spaces or characters)
text =  "Python"
print(text.rjust(10, "*"))                  # rjust()


# rjust() (Right-aligns the string within a specified width, padding with spaces or characters)
text =  "Python"
print(text.ljust(10, "*"))                  # ljust()


# zfill() (Pads a numeric string on the left with zeros until it reaches a given length)
num = "42"
print(num.zfill(5))                         # zfill()


# isalpha() (Checks if the string contains only letters)
print("Lagos".isalpha())               # True
print("Lagos123".isalpha())            # False


# isdigits() (Checks if the string contains only digits)
print("12345".isdigit())              # True
print("123ab".isdigit())              # False


# isalnum() (Checks it the string contains only letters and digits)
print("Python3".isalnum())          # True
print("Python 3".isalnum())         # False


# isspace() (Checks if there's anything typed inside the double qoutes)
print(" ".isspace()) # True
print("My Love".isspace()) # False


# islower() (Checks if its in lower case)
print("My name".islower())        # False 
print("my name".islower())        # True


# isupper() (Checks if the string contains uppercase)
print("PYTHON".isupper())          # True
print("Python".isupper())          # False
print("python".isupper())          # False


# istitle() (Checks if the first letters are in capital letter)
print("Janet is Beautiful".istitle())       # False
print("Janet is beautiful".istitle())       # False
print("Janet Is Bautiful".istitle())        # True
print("JANET IS BEAUTIFUL".istitle())       # False
print("janet is beautiful".istitle())       # False