try:
    #Taking input from user
    number=int(input("enter a number: "))

    if number<0:
        print("Factorial is not defined for neagtive numbers. ")

    elif number == 0:
        print("0!=1")

    else:
        factorial=1
        steps="" # To store multiplication steps

        for i in range(number,0,-1):
            factorial*=i
            steps+=str(i)

            if i!=1:
                steps +=" x "

        #Display result
        print(f"{number}!={steps}={factorial}")

except ValueError:
    print("Plaese enter a valid integer")