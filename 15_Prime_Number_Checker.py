#Prime Number checker

def is_prime(num):
    # Numbers less than 2 are not prime
    if num < 2:
        return False

    # 2 is the only even prime number
    if num == 2:
        return True

    # Even numbers greater than 2 are not prime
    if num % 2 == 0:
        return False

    # Check divisibility up to square root
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True


try:
    # -------- PART 1 --------
    number = int(input("Enter a number: "))

    if is_prime(number):
        print(f"{number} is a PRIME number ✅")
    else:
        print(f"{number} is NOT a prime number ❌")

    # -------- PART 2 --------
    start = int(input("\nEnter start range: "))
    end = int(input("Enter end range: "))

    if start > end:
        print("Invalid range.")
    else:
        primes = []

        # Find primes in range
        for n in range(start, end + 1):
            if is_prime(n):
                primes.append(n)

        # Display result
        print("Prime numbers:", ", ".join(map(str, primes)))

except ValueError:
    print(" Please enter valid integers only.")