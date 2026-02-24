# Sum_Average_Calculator

try:
    # Ask how many numbers
    count=int(input("How many numbers? "))

    if count<=0:
        print("Number count must be greater than 0")

    else:
        numbers=[]
        
        # Taking inputs using loop
        for i in range(1,count+1):
            num=float(input(f"Enter number {i}: "))
            numbers.append(num)
        
        #Calculations
        total_sum=sum(numbers)
        average=total_sum/len(numbers)
        maximum=max(numbers)
        minimum=min(numbers)

        # Display results
        print("\n===== RESULTS =====")
        print("Sum:", total_sum)
        print("Average:", average)
        print("Maximum:", maximum)
        print("Minimum:", minimum)

except ValueError:
    print(" Invalid input! Please enter numeric values ")