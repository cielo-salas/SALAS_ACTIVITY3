# Prompt the user to enter purchase amount

amount = float(input("Enter the purchase amount: "))

# Compute the sales tax (6%)

sales_tax = amount * 0.06

# Display the sales tax with two decimal point

print("sales_tax: ", round(sales_tax, 2))
