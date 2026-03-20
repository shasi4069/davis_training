# Function definitions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


# Main program
while True:
    print("\n===== MENU DRIVEN CALCULATOR =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting calculator... Thank you!")
        break

    # Check valid option
    if choice == '1' or choice == '2' or choice == '3' or choice == '4':
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Operation selection using if-elif
        if choice == '1':
            print("Result:", add(num1, num2))

        elif choice == '2':
            print("Result:", subtract(num1, num2))

        elif choice == '3':
            print("Result:", multiply(num1, num2))

        elif choice == '4':
            print("Result:", divide(num1, num2))

    else:
        print("Invalid choice! Please enter 1 to 5.")