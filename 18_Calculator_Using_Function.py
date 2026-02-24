#Calculator Using Function

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    #Handle divisible by 0
    if b==0:
        return " Divisible by zero not allowed"
    
    return a/b

def modulus(a,b):
    if b==0:
        return " Modulus by zero not allowed"
    
    return a%b

def power(a,b):
    return a**b

def calculator():
    while True:
        try:
            print("\n===== FUNCTION CALCULATOR =====")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Modulus")
            print("6. Power")
            print("7. Exit")

            choice = int(input("Enter your choice (1-7): "))

            # Exit option
            if choice == 7:
                print("Calculator closed ")
                break

            # Take numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Call appropriate function
            if choice == 1:
                result = add(num1, num2)

            elif choice == 2:
                result = subtract(num1, num2)

            elif choice == 3:
                result = multiply(num1, num2)

            elif choice == 4:
                result = divide(num1, num2)

            elif choice == 5:
                result = modulus(num1, num2)

            elif choice == 6:
                result = power(num1, num2)

            else:
                print(" Invalid choice.")
                continue

            # Display result
            print("Result:", result)

        except ValueError:
            print("Invalid input! Enter numeric values.")

calculator()
