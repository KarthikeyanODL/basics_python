def book_ticket():
    # 1. Get details from the user
    movie = input("Enter movie name: ")
    price = float(input("Enter ticket price: "))  # Convert string to float
    seat = int(input("Enter seat number: "))      # Convert string to int
    
    # Simple check for availability
    is_available = True 

    # 2. Logic
    if is_available:
        print(f"\nSuccess! Booking seat {seat} for '{movie}'.")
        print(f"Total cost: {price} INR")
    else:
        print("Sorry, this seat is already taken.")

# Call the function
book_ticket()

