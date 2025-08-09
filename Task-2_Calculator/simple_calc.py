def calculator():
    print("Simple Calculator")
    print("------------------")

    while True:
        try:
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))

            print("\nChoose an operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. Exit")

            choice = input("Enter choice (1/2/3/4/5): ")

            if choice == '1':
                result = num1 + num2
                print(f"\nResult: {num1} + {num2} = {result}")

            elif choice == '2':
                result = num1 - num2
                print(f"\nResult: {num1} - {num2} = {result}")

            elif choice == '3':
                result = num1 * num2
                print(f"\nResult: {num1} * {num2} = {result}")

            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is undefined.")
                else:
                    result = num1 / num2
                    print(f"\nResult: {num1} / {num2} = {result}")

            elif choice == '5':
                print("\nExiting the calculator. Goodbye!")
                break

            else:
                print("Invalid choice. Please select a valid option (1-5).")

        except ValueError:
            print("Invalid input! Please enter numeric values for numbers.")

# Run the calculator
calculator()
