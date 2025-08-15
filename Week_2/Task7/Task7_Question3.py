# Days and Activities Pairing**
# Requirements:
# Use a tuple for days.
# Use {day: activity for day, activity in `zip(..., ...)`}.#Tip: Research on how to use `zip()`


# Store days of the week in a tuple and ask the user to input an activity for three specific days.
print("The days of the week are:")
days_of_the_week = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
print(days_of_the_week) 

# Input an activity for three specific days.
print("\nDear user, please input an activity for three specific days:")
activity1 = input("Input the activity for monday: ")
activity2 = input("Input the activity for wednesday: ")
activity3 = input("Input the activity for friday: ")
activities = (activity1, activity2, activity3)

# Use dictionary comprehension to pair days and activities.
print("\nThe daily activities are:")
daily_activities = {"sunday": "no activity", "monday": activity1, "tuesday": "no activity", "wednesday": activity2, "thursday": "no activity", "friday": activity3, "saturday": "no activity"}
for key, value in daily_activities.items():
    print(f"{key}: {value}")

# Print the dictionary using dict(zip..., ...)
print("\nWhile the activities for the three specific days are:")
days_activities = dict(zip(days_of_the_week, activities))
print(days_activities)















