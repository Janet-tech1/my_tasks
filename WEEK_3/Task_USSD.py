# USSD code response
print("Welcome to Zenith Bank")  # Welcome message
balance  = 9000

while True: 
    print("\nATM Menu:")
    print("1. Check account")
    print("2. Airtime and Data")
    print("3. Transfer")
    print("4. Withdraw")
    print("5. Exit")
    order = (input("Enter choice: "))

    if order == "1":
        print(f"Your balance is: {balance}")   
    elif order == "2":
        amount = int(input("Enter airtime amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Airtime purchase successful. New balance: {balance}")
        else:
            print("Insufficient funds")
    elif order == "3":
        amount = int(input("Enter amount you want to transfer: "))
        if amount <= balance:
            balance -= amount
            print(f"Transfer successful. New balance: {balance}")
        else:
            print("Insuffient funds")
    elif order == "4":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. New balance: {balance}")
        else:
            print("Insufficient funds.")
    elif order == "5":
        print("Thank you for using our ATM. Goodbye!") 
        break 
    else: 
        print("Invalid option. Try again.")



   










# if order == 3:{
#     print(num3)
# }
# elif order == 4:{
#     print(num4)
# }
# if order == 5:{
#     print("Register")
# }
# if order == 6:{
#     print("Betting and Utilities")
# }
# if order == 7:{
#     print("Total assests")
# }
# if order == 8:{
#     print("Add Money")
# }
# if order == 9:{
#     print("Withdraw")
# }
# if order == 0:{
#     print("Next")
# }   
# print(" Please,type in your pin")