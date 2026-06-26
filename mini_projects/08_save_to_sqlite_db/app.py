# We need these tools to build our app
from flask import Flask, render_template, request, jsonify
import sqlite3

# Create the Flask app
app = Flask(__name__)


# --------------------------------------------------
# STEP 1: Create the database and table
# (This runs only once when the app starts)
# --------------------------------------------------
def create_database():
    # Connect to the database file (creates the file if it doesn't exist)
    conn = sqlite3.connect('details.db')

    # Create a table to store name, email, city
    conn.execute('''
        CREATE TABLE IF NOT EXISTS details (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT,
            email TEXT,
            city  TEXT
        )
    ''')

    # Save the changes
    conn.commit()

    # Close the connection
    conn.close()


# --------------------------------------------------
# STEP 2: Show the HTML page when user opens the app
# --------------------------------------------------
@app.route('/')
def home():
    return render_template('index.html')


# --------------------------------------------------
# STEP 3: Receive data from browser and save to DB
# --------------------------------------------------
@app.route('/submit', methods=['POST'])
def submit():

    # Get the data sent from the browser
    data = request.get_json()

    name  = data['name']
    email = data['email']
    city  = data['city']

    # Connect to the database
    conn = sqlite3.connect('details.db')

    # Save the data into the table
    conn.execute(
        'INSERT INTO details (name, email, city) VALUES (?, ?, ?)',
        (name, email, city)
    )

    # Save the changes
    conn.commit()

    # Count how many rows are saved so far
    total = conn.execute('SELECT COUNT(*) FROM details').fetchone()[0]

    # Close the connection
    conn.close()

    # Print in terminal so we can see what was received
    print("Received from browser:")
    print("  Name  :", name)
    print("  Email :", email)
    print("  City  :", city)

    # Send a response back to the browser
    return jsonify({
        "message": f"Details saved for {name}!",
        "total": total
    })


# --------------------------------------------------
# Start the app
# --------------------------------------------------
if __name__ == '__main__':
    create_database()   # Create DB before starting
    app.run(debug=True)
