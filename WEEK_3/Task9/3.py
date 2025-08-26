# Create a tuple of 5 Geopolitical zones in Nigeria entered by the user.
print("Hello dear, please input 5 Geopolitical zones in Nigeria:")
zone1 = input("Enter the first geopolitical zone:")
zone2 = input("Enter the second geopolitical zone:")
zone3 = input("Enter the third geopolitical zone:")
zone4 = input("Enter the fourth geopolitical zone:")
zone5 = input("Enter the fifth geopolitical zone:")
zones = (zone1, zone2, zone3, zone4, zone5) 
print(zones)


# Check if "South West" is in the tuple and print "Yes" or "No".
print("\nIs South West in the zones listed?")
if ("South West" in zones):
    print("Yes")
elif ("South West" not in zones):
    print("No")
