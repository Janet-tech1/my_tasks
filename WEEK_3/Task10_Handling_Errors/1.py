# USSD code response
print("Welcome to Zenith Bank")  # Welcome message
balance  = 9000

while True: 
    print("\nATM Menu:")
    print("1. Check account")
    print("2. Airtime")
    print("3. Transfer")
    print("4. Withdraw")
    print("5. Data")
    print("6. Exit")
    order = (input("Enter choice: "))
    
    if order == "1":
        
    # ValueError – Invalid value for a function.
        pin = int("five hundred naira")            # cannot convert string to int
        print(f"Your balance is: #{balance}")  
         
    elif order == "2":
        amount = int(input("Enter airtime amount: "))
        if amount <= balance:
            balance -= amount
            pin = int(input("Enter your pin: "))
            print(f"You have successfully purchased: #{amount} airtime. New balance: {balance}")
        else:
            print("Insufficient funds")

    elif order == "3":
        amount = int(input("Enter the amount you want to transfer: "))
        if amount <= balance:
            balance -= amount
            acct_num = int(input("Enter the account number: "))
            acct_name = input("Enter the account name:")
            pin = int(input("Enter your pin: "))
            print(f"You have successfully transfered: #{amount} to {acct_name}. New balance: {balance}")
        else:
            print("Insuffient funds")

    elif order == "4":
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            pin = int(input("Enter your pin: "))
            print(f"Withdrawal successful. New balance: {balance}")
        else:
            print("Insufficient funds.")

    elif order == "5":
        amount = int(input("Enter data amount: "))
        if amount <= balance:
            balance -= amount
            pin = int(input("Enter your pin: "))
            print(f"You have successfully purchased: #{amount} data. New balance: {balance}")
        else:
            print("Insufficient funds")     

    elif order == "6":
        print("Thank you for using our ATM. Goodbye!") 
        break 
    else: 
        print("Invalid option. Try again.")


