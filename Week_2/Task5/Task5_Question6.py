# Attendance tracker: Write a Python program that;

# 1. Stores the days of the week in a tuple.
day_week = ("Sunday", "Monday", "Tuesday", "Wednesday","Thursday", "Friday", "Saturday")
print(day_week)

# Stores the months of the year in another tuple.
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November")
print(months)

# Asks the user to enter
print("Hello dear friend, please provide the following information.")
name = input("Enter your first name:")
gender = input("Enter your gender:")
course_track = input("Enter your course track:")
current_month_num = int(input("Enter the current month number:"))
current_day_num = int(input("Enter the current day number:"))

info = (name, gender, course_track, current_month_num, current_day_num)
print(info)
# person = (info)
# name,gender,course_track,current_month_num,current_day_num = person
print("\nThis Is The Attendance Tracker For The New Month.")
print(f"Name: {name}.")             
print(f"Gender: {gender}.")               
print(f"Course track: {course_track}.")  
print(f"Current month number: {current_month_num}.")              
print(f"Current day number: {current_day_num}.")


