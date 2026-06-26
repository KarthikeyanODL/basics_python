from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'data.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    new_entry = request.get_json()

    all_data = load_data()
    all_data.append(new_entry)
    save_data(all_data)

    print(f"Saved: {new_entry}")
    return jsonify({"status": "success", "message": f"Details saved for {new_entry['name']}!", "total": len(all_data)})

if __name__ == '__main__':
    app.run(debug=True)
