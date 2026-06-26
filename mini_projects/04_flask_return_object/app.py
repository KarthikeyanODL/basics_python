from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_object():
    person = {
        "name": "Karthikey",
        "age": 25,
        "language": "Python"
    }
    return jsonify(person)

if __name__ == '__main__':
    app.run(debug=True)
