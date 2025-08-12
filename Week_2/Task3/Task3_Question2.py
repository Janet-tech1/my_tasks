# 6. Check if a given string contains the substring "python" (case-insensitive)
text = "I am learning python programming"
substring = "python"
index = text.index(substring)
print(f"Substring found at index: {index}")


# 7. Write a program to reverse a string without using slicing
word = "Welcome"
letter1 = (word[-1])          # e
letter2 = (word[-2])          # m
letter3 = (word[-3])          # o
letter4 = (word[-4])          # c
letter5 = (word[-5])          # l
letter6 = (word[-6])          # e
letter7 = (word[-7])          # W
print(letter1 + letter2 + letter3 + letter4 + letter5 + letter6 + letter7)


# 8. Given a string with extra spaces, remove the leading trailing spaces
text = "   I love London   "
print(text.strip())


# 9. Ask the user to enter a sentence and print the number of vowels in it
sentence = "I love pounded yam"
count1 = sentence.count('a')
count2 = sentence.count('e')
count3 = sentence.count('i')
count4 = sentence.count('o')
count5 = sentence.count('u')
print(count1 + count2 + count3 + count4 + count5)


# 10. Convert a string "1234" to an integer and multiply it by 2
str_num = "1234"
int_num = int(str_num)
solution = int_num * 2
print(solution)
