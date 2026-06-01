# Use Case: A Movie Ticket Booking System

movie_title = "Blast"      # str: The name of the movie
ticket_price = 250.50          # float: The price in dollars
seat_number = 42               # int: The specific seat location
is_available = True            # bool: Check if the seat is free

# Logic: Can the user book this seat?
if is_available:
    print(f"Booking seat number {seat_number} for '{movie_title}' movie.")
    print(f"Total cost: {ticket_price} INR")
else:
    print("Sorry, this seat is already taken.")

