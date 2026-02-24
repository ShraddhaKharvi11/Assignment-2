# Leap Year Checker

try:
    # Taking input from user
    year=int(input("Enter a year: "))

    # Leap year logic
    if (year % 4 == 0) and (year % 100!=0 or year % 400 == 0):
        print("\n Year: ",year)
        print("Result: Leap Year")

        # Explaining reason
        if year % 400 ==0:
            print("Reason: Divisible by 400(special leap year rule). ")
        else:
            print("Reason: Divisible by $ but not divisble by 100")

    else:
        print("\n Year: ",year)
        print("Result: NOT a Leap Year")

        if year % 4!=0:
            print("Reason: Not divisible by 4. ")

        elif year % 100==0 and year % 400!=0:
            print("Reason: Divisible by 100 but not by 400")

except ValueError:
    print(" Invalid input! Plaese enter a valid yaer") 