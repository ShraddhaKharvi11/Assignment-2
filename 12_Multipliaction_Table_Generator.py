# Multiplication Table Generator

try:
    #Taking Input
    number=int(input("Enter number: "))
    end_range=int(input("Enter range (end):"))

    if end_range<=0:
        print("Range must be positive")

    else:
        print(f"\nMultiplication Table of {number}")
        
        #Genearting multipliation table
        for i in range(1,end_range+1):
            result=number*i
            print(f"{number} x {i} = {result}")

except ValueError:
    print("Please enter valid integer")