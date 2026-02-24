while True:
    try:
        print("\n===== NUMBER PATTERN PRINTER =====")
        print("1. Pattern 1")
        print("2. Pattern 2")
        print("3. Pattern 3")
        print("4. Pattern 4")
        print("5. Exit")

        choice = int(input("Choose pattern (1-5): "))

        if choice == 5:
            print("Program exited ✅")
            break

        n = int(input("Enter height: "))

        if n <= 0:
            print(" Height must be positive.")
            continue

        if choice == 1:
            print("\nPattern 1:")
            for i in range(1, n + 1):
                for j in range(1, i + 1):
                    print(j, end=" ")
                print()

        elif choice == 2:
            print("\nPattern 2:")
            for i in range(1, n + 1):
                for j in range(i):
                    print(i, end=" ")
                print()

        elif choice == 3:
            print("\nPattern 3:")
            for i in range(n, 0, -1):
                for j in range(i, 0, -1):
                    print(j, end=" ")
                print()

        elif choice == 4:
            print("\nPattern 4:")
            for i in range(1, n + 1):
                # Increasing numbers
                for j in range(1, i + 1):
                    print(j, end="")
                # Decreasing numbers
                for j in range(i - 1, 0, -1):
                    print(j, end="")
                print()
        
        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter valid number")