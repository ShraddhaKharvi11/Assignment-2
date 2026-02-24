# Temperature Converter

while True:
    try:
        # Display menu
        print("\n ===== TEMPERATURE CONVERTER =====")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius") 
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")

        # User Choice
        choice=int(input("Enter youe choice(1-7): "))
     
        # Exit Condition
        if choice==7:
            print("Exiting program....")
            break

        temperature=float(input("Enter temperature value: "))

        if choice == 1:
            result=(temperature*9/5)+32
            print(f"Result: {result:.2f} F")

        elif choice == 2:
            result=(temperature-32)*5/9
            print(f"Result: {result:.2f} C")

        elif choice == 3:
            result=temperature+273.15
            print(f"Result: {result:.2f} K")

        elif choice == 4:
            result=temperature-273.15
            print(f"Result: {result:.2f} C")

        elif choice == 5:
            result=(temperature-32)* 5/9 + 273.15
            print(f"Result: {result:.2f} K")

        elif choice == 6:
            result=(temperature-273.15)*9/5 + 32
            print(f"Result: {result:.2f} F")

        else:
            print(" Invalid Choce! Please select 1-7")

    except ValueError:
        print("Invalid input! Please enter numeric values")
            


            
