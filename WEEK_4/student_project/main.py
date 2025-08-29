# main.py → Project entry point

# main.py

import my_data
import my_utils

# Add some students
my_data.add_student("Paul", "AI Engineering")
my_data.add_student("Blessing", "AI Development")

# Print formatted student records
for s in my_data.get_students():
    print(my_utils.format_student(s))