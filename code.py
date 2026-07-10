def calculator():
    print("\n" + "="*40)
    print("      PYTHON CALCULATOR")
    print("="*40)

    while True:
        try:
            num1 = float(input("\nEnter First Number: "))
            num2 = float(input("Enter Second Number: "))

            print("\nChoose Operation")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. Power (^)")
            print("6. Modulus (%)")

            choice = input("\nEnter Choice (1-6): ")

            if choice == '1':
                result = num1 + num2
                op = "+"
            elif choice == '2':
                result = num1 - num2
                op = "-"
            elif choice == '3':
                result = num1 * num2
                op = "*"
            elif choice == '4':
                if num2 == 0:
                    print("Cannot divide by zero!")
                    continue
                result = num1 / num2
                op = "/"
            elif choice == '5':
                result = num1 ** num2
                op = "^"
            elif choice == '6':
                result = num1 % num2
                op = "%"
            else:
                print("Invalid Choice!")
                continue

            print("\n" + "-"*40)
            print(f"Result: {num1} {op} {num2} = {result}")
            print("-"*40)

            again = input("\nPerform Another Calculation? (y/n): ")
            if again.lower() != 'y':
                print("\nThank You For Using Calculator!")
                break

        except ValueError:
            print("Please Enter Valid Numbers!")

calculator()
