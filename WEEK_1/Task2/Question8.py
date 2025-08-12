# Transport fare calculator
distance = float(input("Enter distance in km:"))
fare = float(input("Enter fare per km:"))

total_fare = distance*fare

print(f"Total Fare: #{distance*fare:,.2f}")