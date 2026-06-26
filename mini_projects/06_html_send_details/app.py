from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


# --------------------------------------------------
# WAY 1 - Receive data sent from a HTML Form
# --------------------------------------------------
@app.route('/submit-form', methods=['POST'])
def submit_form():

    # Get the form data sent from the browser
    name  = request.form['name']
    email = request.form['email']
    city  = request.form['city']

    print("Received from HTML Form:")
    print("  Name  :", name)
    print("  Email :", email)
    print("  City  :", city)

    return f"Form received! Hello {name}, from {city}."


# --------------------------------------------------
# WAY 2 - Receive data sent as JSON (fetch)
# --------------------------------------------------
@app.route('/submit-json', methods=['POST'])
def submit_json():

    # Get the JSON data sent from the browser
    data  = request.get_json()
    name  = data['name']
    email = data['email']
    city  = data['city']

    print("Received from JSON fetch:")
    print("  Name  :", name)
    print("  Email :", email)
    print("  City  :", city)

    return jsonify({"message": f"JSON received! Hello {name}, from {city}."})


if __name__ == '__main__':
    app.run(debug=True)
