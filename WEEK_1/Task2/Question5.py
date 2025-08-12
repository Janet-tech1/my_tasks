# Ask for market details
market_name = input("Enter market name:")
num_traders = int(input("Enter number of traders:"))
daily_revenue = float(input("Enter daily revenue in naira:"))

print(f"Market Report for {market_name} market:")
print(f"Number of Traders:{num_traders}")
print(f"Daily Revenue:#{daily_revenue:,.2f}")