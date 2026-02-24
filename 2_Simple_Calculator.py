#Simple Calculator

#Taking input from user and converting to integer
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

#Performing Arthimetic operations
Addition=num1+num2        # Adds two numbers
Subtraction=num1-num2     # Subtracts second number from first
Multiplication=num1*num2  # Multiplies two numbers
Division=num1/num2        # Divides first number by second
Modulus=num1%num2         # Gives remainder after division
Exponentiation=num1**num2 # Exponentiation of number
print("\nResult")
print(f"{num1} + {num2} = {Addition}")
print(f"{num1} - {num2} = {Subtraction}")
print(f"{num1} * {num2} = {Multiplication}")
print(f"{num1} / {num2} = {Division:.2f}")
print(f"{num1} % {num2} = {Modulus}")
print(f"{num1} ^ {num2} = {Exponentiation}")
