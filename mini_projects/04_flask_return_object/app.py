from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_object():
    gold_rate = {
        "gold_24k": 89500.00,
        "gold_22k": 82002.00,
        "silver":   95000.00,
        "unit":     "INR",
        "date":     "2024-01-01"
    }
    return jsonify(gold_rate)

if __name__ == '__main__':
    app.run(debug=True)
