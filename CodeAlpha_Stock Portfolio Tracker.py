# Dictionary to store stock data
# Format: { "STOCK_NAME": total_value }
portfolio = {}

def add_stock():
    print("\n➕ Add New Stock")

    stock_name = input("Enter stock name (e.g. AAPL): ").upper()

    # Input validation for quantity
    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per stock: "))
    except ValueError:
        print("❌ Please enter valid numbers for quantity and price.")
        return

    if quantity <= 0 or price <= 0:
        print("❌ Quantity and price must be greater than zero.")
        return

    investment_value = quantity * price

    # Store or update stock value
    if stock_name in portfolio:
        portfolio[stock_name] += investment_value
    else:
        portfolio[stock_name] = investment_value

    print(f"✅ {stock_name} added successfully!")
    print(f"Investment Value: {investment_value}")

def show_portfolio():
    if not portfolio:
        print("\n📭 Portfolio is empty.")
        return

    print("\n📊 Your Stock Portfolio")
    print("-" * 30)

    total_investment = 0

    for stock, value in portfolio.items():
        print(f"{stock} : {value}")
        total_investment += value

    print("-" * 30)
    print(f"💰 Total Investment: {total_investment}")

def main_menu():
    while True:
        print("\n==============================")
        print("📈 STOCK PORTFOLIO TRACKER")
        print("==============================")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_stock()
        elif choice == "2":
            show_portfolio()
        elif choice == "3":
            print("\n👋 Exiting program. Thank you!")
            break
        else:
            print("❌ Invalid choice! Please select 1, 2, or 3.")


main_menu()
