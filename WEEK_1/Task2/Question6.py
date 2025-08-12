# Ask for customer details
name = input("Enter customer's full name:")
units = int(input("Enter units consumed (kWh):"))
cost_per_unit = float(input("Enter cost per unit:"))
total_bill = units*cost_per_unit

print(f"Electricity Bill Receipt\n-------------\nCustomer Name: {name}\nUnits Consumed: {units}kWh\nRate:#{cost_per_unit:.2f} per unit\nTotal Bill:#{total_bill:,.2f}\n---------")