# Advancd Nigerian currency converter
amount_naira = float(input("Enter amount in naira:"))
exchange_rate_usd = float(input("Enter exchange rate to USD:"))
exchange_rate_gbp = float(input("Enter exchange rate to GBP:"))

# Convert to USD and GBP
amount_usd = amount_naira / exchange_rate_usd
amount_gbp = amount_naira / exchange_rate_gbp

print(f"Naira Amount: #{amount_naira:,.2f}")
print(f"USD Equivalent: ${amount_usd:,.2f}")
print(f"GBP Equivalent: €{amount_gbp:,.2f}")
