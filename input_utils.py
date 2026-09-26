def input_price():
    while True:
        try:
            amount = float(input("Enter amount: ₹"))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return amount
        except ValueError:
            print("Invalid input! Please enter a number.")