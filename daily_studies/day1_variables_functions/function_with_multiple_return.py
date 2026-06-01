def process_booking(price, quantity):
    total = price * quantity
    
    # Simple logic: If more than 5 tickets, give 10% discount
    if quantity > 5:
        discount = total * 0.10
        final_price = total - discount
        is_discounted = True
    else:
        final_price = total
        is_discounted = False
        
    # Return TWO values (tuple)
    return final_price, is_discounted

# --- Main Program ---
price = float(input("Enter ticket price: "))
qty = int(input("Enter quantity: "))

# Unpack the two returned values into two variables
total_bill, discount_applied = process_booking(price, qty)

print(f"\n--- Final Receipt ---")
print(f"Total to pay: {total_bill} INR")
print(f"Discount applied: {discount_applied}")

