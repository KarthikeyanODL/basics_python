def calculate_total_cost(price, quantity):
    # Perform the math
    total = price * quantity
    # Send the result back to the caller
    return total

# 1. Get input from the user
movie = input("Enter movie name: ")
ticket_price = float(input("Enter ticket price: "))
tickets_wanted = int(input("How many tickets do you need? "))

# 2. Call the function and store the 'returned' value in a variable
final_bill = calculate_total_cost(ticket_price, tickets_wanted)

# 3. Use the returned value
print(f"\n--- Booking Summary ---")
print(f"Movie: {movie}")
print(f"Total to pay: {final_bill} INR")

