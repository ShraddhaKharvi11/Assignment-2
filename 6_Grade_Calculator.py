# Grade Calculator

try:
    #Taking marks input from user
    subject1=float(input("Enter marks for Subject 1: "))
    subject2=float(input("Enter marks for Subject 2: "))
    subject3=float(input("Enter marks for Subject 3: "))
    subject4=float(input("Enter marks for Subject 4: "))
    subject5=float(input("Enter marks for Subject 5: "))

    # Store marks in a list for easy processing
    marks=[subject1,subject2,subject3,subject4,subject5]

    for mark in marks:
        if mark < 0 or mark >100:
            print("Marks must be between 0 and 100")
            exit()

    total_marks=sum(marks)
    percentage=total_marks/len(marks)

    if percentage>=90:
        grade="A+ (Outstanding)"
    elif percentage>=80:
        grade="A (Excellent)"
    elif percentage>=70:
        grade="B (Good)"
    elif percentage>=60:
        grade="C (Average)"
    elif percentage>=50:
        grade="D (Pass)"
    else:
        grade="F (Fail)"

    if all(mark>=40 for mark in marks):
        result="Pass"
    else:
        result="Fail"

    print("\n ==== RESULT SUMMARY ====")
    print("Marks in each subject: ")
    for i, mark in enumerate(marks,start=1):
        print(f"Subject{i}: {mark}")

    print(f"\nTotal Marks: {total_marks}/500")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print(f"Result: {result}")

except ValueError:
    print("Invalid input! Please enter numeric marks only.")