import csv
from datetime import datetime

def stock_portfolio_tracker():
    # Hardcoded stock prices dictionary
    stock_prices = {
        "AAPL": 180.50,    # Apple Inc.
        "TSLA": 250.75,    # Tesla Inc.
        "GOOGL": 135.20,   # Alphabet Inc.
        "MSFT": 420.30,    # Microsoft Corp.
        "AMZN": 145.80,    # Amazon.com Inc.
        "NVDA": 875.40,    # NVIDIA Corp.
        "META": 315.25,    # Meta Platforms Inc.
        "NFLX": 485.60,    # Netflix Inc.
        "AMD": 125.90,     # Advanced Micro Devices
        "INTC": 35.45      # Intel Corp.
    }
    
    portfolio = {}
    total_value = 0
    
    print("="*50)
    print("      STOCK PORTFOLIO TRACKER")
    print("="*50)
    print("\nAvailable stocks and their current prices:")
    print("-" * 40)
    
    # Display available stocks
    for symbol, price in stock_prices.items():
        print(f"{symbol:<8} ${price:>8.2f}")
    
    print("-" * 40)
    print("\nEnter your stock holdings:")
    print("(Type 'done' when finished)")
    
    # Get user input for portfolio
    while True:
        stock_symbol = input("\nEnter stock symbol: ").upper().strip()
        
        if stock_symbol.lower() == 'done':
            break
        
        # Check if stock exists in our price dictionary
        if stock_symbol not in stock_prices:
            print(f"Sorry, {stock_symbol} is not available in our database.")
            print("Available stocks:", ", ".join(stock_prices.keys()))
            continue
        
        try:
            quantity = int(input(f"Enter quantity of {stock_symbol} shares: "))
            if quantity <= 0:
                print("Please enter a positive number of shares.")
                continue
        except ValueError:
            print("Please enter a valid number for quantity.")
            continue
        
        # Add to portfolio (if stock already exists, add to existing quantity)
        if stock_symbol in portfolio:
            portfolio[stock_symbol] += quantity
            print(f"Added {quantity} more shares of {stock_symbol}. Total: {portfolio[stock_symbol]} shares")
        else:
            portfolio[stock_symbol] = quantity
            print(f"Added {quantity} shares of {stock_symbol} to your portfolio.")
    
    # Calculate and display portfolio summary
    if not portfolio:
        print("\nNo stocks added to portfolio. Goodbye!")
        return
    
    print("\n" + "="*60)
    print("                PORTFOLIO SUMMARY")
    print("="*60)
    print(f"{'Stock':<8} {'Shares':<8} {'Price':<10} {'Total Value':<12}")
    print("-" * 60)
    
    for stock_symbol, quantity in portfolio.items():
        price = stock_prices[stock_symbol]
        stock_value = quantity * price
        total_value += stock_value
        
        print(f"{stock_symbol:<8} {quantity:<8} ${price:<9.2f} ${stock_value:<11.2f}")
    
    print("-" * 60)
    print(f"{'TOTAL PORTFOLIO VALUE:':<38} ${total_value:.2f}")
    print("="*60)
    
    # Ask if user wants to save to file
    save_option = input("\nWould you like to save this portfolio to a file? (y/n): ").lower()
    
    if save_option in ['y', 'yes']:
        file_format = input("Save as (1) Text file or (2) CSV file? Enter 1 or 2: ")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if file_format == "1":
            save_to_txt(portfolio, stock_prices, total_value, timestamp)
        elif file_format == "2":
            save_to_csv(portfolio, stock_prices, total_value, timestamp)
        else:
            print("Invalid option. Portfolio not saved.")

def save_to_txt(portfolio, stock_prices, total_value, timestamp):
    """Save portfolio to a text file"""
    filename = f"portfolio_{timestamp}.txt"
    
    try:
        with open(filename, 'w') as file:
            file.write("STOCK PORTFOLIO SUMMARY\n")
            file.write("=" * 50 + "\n")
            file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            file.write(f"{'Stock':<8} {'Shares':<8} {'Price':<10} {'Total Value':<12}\n")
            file.write("-" * 50 + "\n")
            
            for stock_symbol, quantity in portfolio.items():
                price = stock_prices[stock_symbol]
                stock_value = quantity * price
                file.write(f"{stock_symbol:<8} {quantity:<8} ${price:<9.2f} ${stock_value:<11.2f}\n")
            
            file.write("-" * 50 + "\n")
            file.write(f"TOTAL PORTFOLIO VALUE: ${total_value:.2f}\n")
        
        print(f"Portfolio saved successfully to {filename}")
        
    except Exception as e:
        print(f"Error saving file: {e}")

def save_to_csv(portfolio, stock_prices, total_value, timestamp):
    """Save portfolio to a CSV file"""
    filename = f"portfolio_{timestamp}.csv"
    
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            
            # Write header
            writer.writerow(['Stock Symbol', 'Shares', 'Price per Share', 'Total Value'])
            
            # Write portfolio data
            for stock_symbol, quantity in portfolio.items():
                price = stock_prices[stock_symbol]
                stock_value = quantity * price
                writer.writerow([stock_symbol, quantity, f"${price:.2f}", f"${stock_value:.2f}"])
            
            # Write total
            writer.writerow(['', '', 'TOTAL:', f"${total_value:.2f}"])
        
        print(f"Portfolio saved successfully to {filename}")
        
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    while True:
        stock_portfolio_tracker()
        
        another_portfolio = input("\nWould you like to create another portfolio? (y/n): ").lower()
        if another_portfolio not in ['y', 'yes']:
            print("Thank you for using Stock Portfolio Tracker! Goodbye!")
            break
        print("\n" + "="*70 + "\n")

# Run the program
if __name__ == "__main__":
    main()
