from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/my-details')
def my_details():
    details = {
        "name":     "Karthikey",
        "age":      25,
        "city":     "Chennai",
        "language": "Python"
    }
    return render_template('details.html', details=details)


if __name__ == '__main__':
    app.run(debug=True)
