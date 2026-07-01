print("Welcome to the calculator!")

while True:

    # First Number
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            break
        except:
            print("Invalid number! Try again!")

    # Second Number
    while True:
        try:
            num2 = int(input("Enter the second number: "))
            break
        except:
            print("Invalid number! Try again!")

    # Operation
    operation = input("Enter operation (+, -, *, /): ")

    # Checking operation
    if operation not in ["+", "-", "*", "/"]:
        print("Invalid operation! Try again!")
        continue

    # Operations
    if operation == "+":
        print("Result:", num1 + num2)

    elif operation == "-":
        print("Result:", num1 - num2)

    elif operation == "*":
        print("Result:", num1 * num2)

    elif operation == "/":
        if num2 == 0:
            print("You can't divide by zero!")
        else:
            print("Result:", num1 / num2)

    # Continue
    decision = input("Continue? (Yes/No): ")

    if decision == "No":
        print("Thank you for using the calculator!")
        break