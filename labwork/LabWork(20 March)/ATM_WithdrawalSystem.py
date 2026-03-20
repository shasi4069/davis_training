def atm_withdrawal():
    pin = 1234  # Set initial PIN
    balance = 10000  # Set initial balance

    entered_pin = int(input("Enter your PIN: "))
    if entered_pin == pin:
        print("PIN accepted.")
        while True:
            print(f"Your current balance is: {balance}")
            withdrawal_amount = int(input("Enter amount to withdraw (or 0 to exit): "))
            if withdrawal_amount == 0:
                print("Exiting...")
                break
            elif withdrawal_amount > balance:
                print("Insufficient Balance...")
            else:
                balance -= withdrawal_amount
                print(f"Please take your cash: {withdrawal_amount}")
    else:
        print("Incorrect PIN.")
