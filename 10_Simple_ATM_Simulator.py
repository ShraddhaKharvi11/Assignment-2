#Simple ATM Simulator

#Initial account balance
balance=10000
MIN_BALANCE=500

while True:
    try:
        # Display ATM menu
        print("\n ====ATM SIMULATOR ==== ")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice=int(input("Enter choice: "))
        
        #check balance
        if choice==1:
            print(f"Current Balance : ₹{balance:.2f}")

        # Deposit money
        elif choice == 2:
            deposit_amount=float(input("Enter amount to deposit: "))

            if deposit_amount <=0:
                print("Invalid deposit amount")
            else:
                balance+=deposit_amount
                print("Deposit successful")
                print(f"Updataed Balance: ₹{balance:.2f}")

        # Withdraw money

        elif choice==3:
            withdraw_amount=float(input("Enter amount to withdra: "))

            if withdraw_amount<=0:
                print("Invalid withdraw amount")
            
            elif balance-withdraw_amount < MIN_BALANCE:
                print("Withdrawal denied ! Minimum balance 500 must reamin")

            else:
                balance-=withdraw_amount
                print("Withdraw successfull")
                print(f" New balance: ₹{balance:.2f}")

        elif choice == 4:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice. Plaese select 1-4")

    except ValueError:
        print("Invalid input! Plaese enter numeric values! ")

