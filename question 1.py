def calculate_max_profit(n, prices):
    # Initialize the minimum price and maximum profit
    min_price = float('inf')
    max_profit = 0
    
    # Iterate over the daily prices
    for price in prices:
        # Update the minimum price if the current price is lower
        min_price = min(min_price, price)
        # Calculate the profit if selling at the current price
        profit = price - min_price
        # Update the maximum profit
        max_profit = max(max_profit, profit)
    
    return max_profit


# Input
n = int(input("Enter the number of days: "))
prices = []
for _ in range(n):
    price = int(input(f"Enter price for day {_ + 1}: "))
    prices.append(price)

# Output
max_profit = calculate_max_profit(n, prices)
print(f"Output : {max_profit}")
