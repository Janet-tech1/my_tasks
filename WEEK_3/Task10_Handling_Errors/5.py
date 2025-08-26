score  = 70
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score > 70:              # Should be >=   
    print("Grade: C")
else:
    print("Grade: F")
# output: Grade F (wrong result)

   