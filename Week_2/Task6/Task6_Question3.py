# Store all seat numbers (1 to 50) in a set.
seat_num = set()

numbers =  set(range(1, 51))
print(numbers)

# Ask users to "book" a seat by entering the number.
print("\nBook a seat by entering a number within the range of 1-50.")
seat_num = int(input("Enter your seat number: "))

# Remove booked seats from the set.
numbers.remove(seat_num)   
print(numbers)

# Show remaining seats after each booking.
seat_num = int(input("Enter your seat number: "))
numbers.remove(seat_num)   
print(numbers)