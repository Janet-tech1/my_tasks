# Simulated USSD Menu Interaction
print("Welcome to MTN Mobile Services!")    # Welcome screen
print("Dial *900# to access our services.")

ussd_code = input("Enter USSD code:")
ussd_code == "*900#"

print("\nMTN Mobile Services Menu:")
print("1. Check Balance")
print("2. Buy Airtime")
print("3. Buy Data")

option = int(input("Choose an option:"))

if option == 1:
    print("Your balance is: #5,000")
elif option == 2:
    amount = float(input("Enter amount of airtime to buy:"))
    print(f"Dear Customer, You have successfully bought airtime worth #{amount:.2f}")
elif option == 3:
    amount = float(input("Enter amount of data to buy:"))
    print(f"Dear Customer, You have successfully bought data worth {amount:.2f}MB")


