# Function definition
def book_ticket(movie, price, seat, available):
    if available:
        print(f"Booking seat number {seat} for '{movie}' movie.")
        print(f"Total cost: {price} INR")
    else:
        print(f"Sorry, seat {seat} for '{movie}' is already taken.")

# Calling the function with your variables
movie_title = "Blast"
ticket_price = 250.50
seat_number = 42
is_available = True

# Execute the function
book_ticket(movie_title, ticket_price, seat_number, is_available)

# You can now easily reuse it for another booking:
book_ticket("Karuppu", 300.00, 10, False)

