# Bill Splitter

try:
    # Taking inputs from user
    total_bill=float(input("Enter total bill: "))
    number_of_people=int(input("Number of people: "))
    tax_percentage=float(input("Tax percentage: "))
    tip_percentage=float(input("Tip percentage: "))

    if total_bill<0 or number_of_people<=0:
        print(" Invalid bill amount or number of people.")

    else:
        # Subtotal (original bill)
        subtotal=total_bill

        # Calculate tax amount
        tax_amount=subtotal*(tax_percentage/100)

        # Bill after adding tax
        bill_after_tax=subtotal+tax_amount

        # Calcualte tip amount
        tip_amount=bill_after_tax*(tip_percentage/100)

        # Final total bill
        total_amount=bill_after_tax+tip_amount

        amount_per_person=total_bill/number_of_people

        # Display Output
        print("\n === BILL BREAKDOWN === ")
        print(f"Subtotal: ₹{subtotal:.2f}")
        print(f"Tax ({tax_percentage}%): ₹{tax_amount:.2f}")
        print(f"After tax: ₹{bill_after_tax:.2f}")
        print(f"Tip ({tip_amount}%): ₹{tip_amount:.2f}")
        print(f"Total: ₹{total_amount:.2f}")
        print(f"Per person : ₹{amount_per_person:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values only.")