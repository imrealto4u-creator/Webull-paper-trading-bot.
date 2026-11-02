
from datetime import datetime

# Virtual trading only
STARTING_BALANCE = 100.00
cash = STARTING_BALANCE
shares = 0
symbol = "AAPL"

# Example prices, not live market data
prices = [150, 148, 146, 149, 153]

print("Trading Bot Simulator")
print("Mode: SIMULATION ONLY")
print("Started:", datetime.now())
print("Starting cash: $", cash)

for price in prices:
    if shares == 0 and price <= 147:
        shares = 0.5
        cash -= shares * price
        print("SIMULATED BUY:", shares, "at", price)

    elif shares > 0 and price >= 152:
        cash += shares * price
        print("SIMULATED SELL:", shares, "at", price)
        shares = 0

final_value = cash + shares * prices[-1]

print("Ending cash: $", round(cash, 2))
print("Portfolio value: $", round(final_value, 2))
print("Profit/Loss: $", round(final_value - STARTING_BALANCE, 2))
print("Simulation complete")

