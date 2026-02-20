# Billing System Program

# Taking input for 3 items from user
item1 = float(input("Enter price of Item 1: $"))
item2 = float(input("Enter price of Item 2: $"))
item3 = float(input("Enter price of Item 3: $"))

total = item1 + item2 + item3

# Initialize discount
discount = 0

# Apply 10% discount if total exceeds $50
if total > 50:
    discount = total * 0.10

final_amount = total - discount

print("\n----- Billing Summary -----")
print(f"Original Total: ${total:.2f}")
print(f"Discount: ${discount:.2f}")
print(f"Final Payable Amount: ${final_amount:.2f}")
print("Thank you! Visit Again 😊")
