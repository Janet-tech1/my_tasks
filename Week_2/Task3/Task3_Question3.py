# 12. Ask the user for a sentence and print each word on a new line
text = "I\nAm\nLearning\nPython\nProgramming"
lines = (text.split('\n'))
print('\n'.join(lines))


# 13. Replace all spaces in a string with underscores(_)
message = "I love singing and dancing"
print(message.replace(" ", "_"))             # replace()


# 14. Count how many times the letter "a" appears in "Banana"
letter = "Banana"
count = letter.count('a')
print(count)


# 15. Check if a given string starts with "https://"
filename = "https://.janet@facebook.com"
print(filename.startswith("https://"))       # True
print(filename.endswith(".janet"))           # False

