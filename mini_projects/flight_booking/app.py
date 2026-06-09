from flask import Flask, render_template, request

app = Flask(__name__)

flights = {
    "AI101": {"source": "Delhi",     "dest": "Mumbai",    "seats": 5,  "price": 5500},
    "AI102": {"source": "Mumbai",    "dest": "Delhi",     "seats": 8,  "price": 5200},
    "6E201": {"source": "Bangalore", "dest": "Chennai",   "seats": 3,  "price": 3200},
    "6E202": {"source": "Chennai",   "dest": "Bangalore", "seats": 4,  "price": 3100},
    "UK301": {"source": "Delhi",     "dest": "Kolkata",   "seats": 2,  "price": 6000},
    "UK302": {"source": "Kolkata",   "dest": "Delhi",     "seats": 6,  "price": 6200},
    "SG401": {"source": "Hyderabad", "dest": "Pune",      "seats": 10, "price": 4000},
    "SG402": {"source": "Pune",      "dest": "Hyderabad", "seats": 7,  "price": 4100},
    "QP501": {"source": "Ahmedabad", "dest": "Delhi",     "seats": 5,  "price": 3500},
    "QP502": {"source": "Delhi",     "dest": "Ahmedabad", "seats": 9,  "price": 3600},
}


# Step 1 - Show search form
@app.route("/")
def home():
    return render_template("search.html")


# Step 2 - Search for a flight
@app.route("/search", methods=["POST"])
def search():
    source      = request.form["source"]
    destination = request.form["destination"]

    for flight_no, details in flights.items():
        if details["source"].lower() == source.lower() and details["dest"].lower() == destination.lower():
            return render_template("flight.html", flight_no=flight_no, details=details)

    return render_template("search.html", error="No flight found for this route.")


# Step 3 - Confirm booking
@app.route("/book", methods=["POST"])
def book():
    flight_no = request.form["flight_no"]
    seats     = int(request.form["seats"])
    details   = flights[flight_no]

    if seats > details["seats"]:
        return render_template("flight.html", flight_no=flight_no, details=details,
                               error=f"Only {details['seats']} seat(s) available.")

    details["seats"] -= seats
    total = seats * details["price"]

    return render_template("success.html", flight_no=flight_no, details=details,
                           seats_booked=seats, total=total)


if __name__ == "__main__":
    app.run(debug=True)
