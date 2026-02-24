try:
    #Take input as string (works for words & numbers)
    user_input=input("Enter word/number: ")

    original=user_input

    processed=user_input.lower()

    reversed_text=processed[::-1]

    print("\nOriginal:", original)
    print("Processed(lowercase): ",processed)
    print("Reveresed: ",reversed_text)

    if processed==reversed_text:
        print("Result: Palindrome")
    else:
        print("Result: Not a Palindrome")

except Exception:
    print("Invalid input")
