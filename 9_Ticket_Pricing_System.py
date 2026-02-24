try:
    # Taking input
    age=int(input("Enter age : "))
    day=input("Enter day of week: ").strip().lower()
    number_of_tickets=int(input("enter number of tickets: "))

    if age < 0 or number_of_tickets <=0:
        print(" Invalid age or ticket count")
    
    if age < 3:
        base_price=0
        category="Free"

    elif 3 <=age <=12:
        base_price=150
        category="Child"

    elif 13 <=age <=59:
        base_price=300
        category="Adult"
    
    else:
        base_price=200
        category="Senior"

    weekend_days=['friday','saturday','sunday']

    if day in weekend_days:
        discount_rate=0.20
    elif day in ['monday','tuesday','wednesday','thursday']:
        discount_rate=0.0
    else:
        print("Invalid day entered")
        exit()

    subtotal=base_price*number_of_tickets
    discount_amount=subtotal*discount_rate
    final_price=subtotal-discount_rate

     # -------- Output --------
    print("\n===== TICKET BILL =====")
    print(f"Category: {category}")
    print(f"Base price per ticket: ₹{base_price:.2f}")
    print(f"Subtotal: ₹{subtotal:.2f}")
    print(f"Discount: ₹{discount_amount:.2f}")
    print(f"Price after discount: ₹{final_price:.2f}")
    print(f"Total amount to pay: ₹{final_price:.2f}")
except ValueError:
    print("Invalid input! Please enter correct values")