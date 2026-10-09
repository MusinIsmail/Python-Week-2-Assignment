# assignment.py

# Collect user inputs
price_input = input("Enter the price of one item ($): ")
quantity_input = input("Enter the quantity desired: ")

# Convert input strings to numeric values
price = float(price_input)
quantity = int(quantity_input)

# Calculate total cost
total = price * quantity

# Display formatted summary using an f-string
print(f"\n{quantity} items at ${price:.2f} each = ${total:.2f}")