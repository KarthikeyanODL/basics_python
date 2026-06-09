from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)
DB = "reports.db"

# ── Setup DB ──────────────────────────────────────────
def init_db():
    conn = sqlite3.connect(DB)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            name   TEXT,
            issue  TEXT,
            status TEXT DEFAULT 'Pending'
        )
    """)
    conn.commit()
    conn.close()

# ── Routes ────────────────────────────────────────────

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name  = request.form.get('name', '')
    issue = request.form.get('issue', '')
    conn = sqlite3.connect(DB)
    conn.execute("INSERT INTO reports (name, issue) VALUES (?, ?)", (name, issue))
    conn.commit()
    conn.close()
    return jsonify({"message": "Report submitted!", "name": name, "issue": issue})

@app.route('/reports')
def reports():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM reports ORDER BY id DESC").fetchall()
    conn.close()
    return render_template('reports.html', reports=[dict(r) for r in rows])

if __name__ == '__main__':
    init_db()
    app.run(debug=True)