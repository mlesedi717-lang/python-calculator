while True:
    try:
        print("\n===== CALCULATOR MENU =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Choose an operation (1-4): ")

        if choice not in ["1", "2", "3", "4"]:
            raise ValueError("Invalid menu choice.")

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            result = num1 + num2
            operation = "Addition"

        elif choice == "2":
            result = num1 - num2
            operation = "Subtraction"

        elif choice == "3":
            result = num1 * num2
            operation = "Multiplication"

        elif choice == "4":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
            operation = "Division"

    except ValueError:
        print("Error: Please enter numeric values and a valid menu option.")
        print("Operation failed.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        print("Operation failed.")

    except Exception as e:
        print("Unexpected error:", e)
        print("Operation failed.")

    else:
        print(f"\n{operation} Result: {result}")
        print("Operation completed successfully.")

    finally:
        again = input("\nWould you like to perform another calculation? (yes/no): ").lower()

        if again != "yes":
            print("Thank you for using the calculator. Goodbye!")
            break

