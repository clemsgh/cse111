from datetime import datetime

DISCOUNT = 0.1
TAX_RATE = 0.06

current_date = datetime.now().weekday()

subtotal = 0
quantity = -1
while quantity != 0:
    quantity = int(input("Enter the quantity of items: "))
    if quantity == 0:
        break
    price = float(input("Enter the price of the item: $"))
    subtotal += round(quantity * price,2)
#subtotal = float(input("What is your subtotal? $"))
print(f"\nTotal order {subtotal}",)

discount = 0

if current_date == 1 or current_date == 2:
    if subtotal >= 50:
        discount = subtotal * DISCOUNT
        print(f"Discount ${discount:.2f}")
    else:
        short = 50 -subtotal
        print(f"Add ${short:.2f} more to your order to qualify for a discount")
subtotal -= discount
tax = subtotal * TAX_RATE
total = subtotal + tax
    
print(f"Tax {tax:.2f}", f"\nTotal Due ${total:.2f}")