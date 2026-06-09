import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

DB = "flights.db"


def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row   # lets us access columns by name: row["source"]
    return conn


def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS flights (
            flight_no  TEXT PRIMARY KEY,
            source     TEXT,
            dest       TEXT,
            seats      INTEGER,
            price      INTEGER
        )
    """)

    # Insert starting data only if table is empty
    if conn.execute("SELECT COUNT(*) FROM flights").fetchone()[0] == 0:
        flights = [
            ("AI101", "Delhi",     "Mumbai",    5,  5500),
            ("AI102", "Mumbai",    "Delhi",     8,  5200),
            ("6E201", "Bangalore", "Chennai",   3,  3200),
            ("6E202", "Chennai",   "Bangalore", 4,  3100),
            ("UK301", "Delhi",     "Kolkata",   2,  6000),
            ("UK302", "Kolkata",   "Delhi",     6,  6200),
            ("SG401", "Hyderabad", "Pune",      10, 4000),
            ("SG402", "Pune",      "Hyderabad", 7,  4100),
            ("QP501", "Ahmedabad", "Delhi",     5,  3500),
            ("QP502", "Delhi",     "Ahmedabad", 9,  3600),
        ]
        conn.executemany(
            "INSERT INTO flights VALUES (?, ?, ?, ?, ?)", flights
        )

    conn.commit()
    conn.close()


# Step 1 - Show search form
@app.route("/")
def home():
    return render_template("search.html")


# Step 2 - Search for a flight
@app.route("/search", methods=["POST"])
def search():
    source      = request.form["source"]
    destination = request.form["destination"]

    conn   = get_db()
    flight = conn.execute(
        "SELECT * FROM flights WHERE LOWER(source) = LOWER(?) AND LOWER(dest) = LOWER(?)",
        (source, destination)
    ).fetchone()
    conn.close()

    if flight:
        return render_template("flight.html", flight=flight)

    return render_template("search.html", error="No flight found for this route.")


# Step 3 - Confirm booking
@app.route("/book", methods=["POST"])
def book():
    flight_no = request.form["flight_no"]
    seats     = int(request.form["seats"])

    conn   = get_db()
    flight = conn.execute(
        "SELECT * FROM flights WHERE flight_no = ?", (flight_no,)
    ).fetchone()

    if seats > flight["seats"]:
        conn.close()
        return render_template("flight.html", flight=flight,
                               error=f"Only {flight['seats']} seat(s) available.")

    conn.execute(
        "UPDATE flights SET seats = seats - ? WHERE flight_no = ?",
        (seats, flight_no)
    )
    conn.commit()

    # Fetch updated row to show remaining seats
    updated_flight = conn.execute(
        "SELECT * FROM flights WHERE flight_no = ?", (flight_no,)
    ).fetchone()
    conn.close()

    total = seats * flight["price"]
    return render_template("success.html", flight=updated_flight,
                           seats_booked=seats, total=total)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
