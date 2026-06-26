from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)


# --------------------------------------------------
# Create the database and table when app starts
# --------------------------------------------------
def create_database():
    conn = sqlite3.connect('students.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT,
            email TEXT,
            city  TEXT
        )
    ''')
    conn.commit()
    conn.close()


# --------------------------------------------------
# Show the main HTML page
# --------------------------------------------------
@app.route('/')
def home():
    return render_template('index.html')


# --------------------------------------------------
# CREATE - Save a new student to the database
# --------------------------------------------------
@app.route('/create', methods=['POST'])
def create():
    data  = request.get_json()
    name  = data['name']
    email = data['email']
    city  = data['city']

    # if/else — validate before saving
    if name == '':
        return jsonify({"message": "Name is required!"})
    elif email == '':
        return jsonify({"message": "Email is required!"})
    elif city == '':
        return jsonify({"message": "City is required!"})
    else:
        conn = sqlite3.connect('students.db')
        conn.execute(
            'INSERT INTO students (name, email, city) VALUES (?, ?, ?)',
            (name, email, city)
        )
        conn.commit()
        conn.close()

        print(f"Created: {name}, {email}, {city}")
        return jsonify({"message": f"Student '{name}' created successfully!"})


# --------------------------------------------------
# READ - Get all students from the database
# --------------------------------------------------
@app.route('/read', methods=['GET'])
def read():
    conn = sqlite3.connect('students.db')
    rows = conn.execute('SELECT id, name, email, city FROM students').fetchall()
    conn.close()

    # for loop — convert each row into a dictionary
    students = []
    for row in rows:
        student = {
            "id":    row[0],
            "name":  row[1],
            "email": row[2],
            "city":  row[3]
        }
        students.append(student)

    print(f"Fetched {len(students)} students")
    return jsonify(students)


# --------------------------------------------------
# SEARCH - Find students by name using for loop
# --------------------------------------------------
@app.route('/search', methods=['POST'])
def search():
    data        = request.get_json()
    search_name = data['name']

    # if/else — check if search input is empty
    if search_name == '':
        return jsonify({"message": "Please enter a name to search!"})

    conn = sqlite3.connect('students.db')
    rows = conn.execute('SELECT id, name, email, city FROM students').fetchall()
    conn.close()

    # for loop — go through every student and check if name matches
    results = []
    for row in rows:
        student_name = row[1]
        if search_name.lower() in student_name.lower():
            results.append({
                "id":    row[0],
                "name":  row[1],
                "email": row[2],
                "city":  row[3]
            })

    # if/else — return message based on results
    if len(results) == 0:
        return jsonify({"message": f"No student found with name '{search_name}'", "results": []})
    else:
        return jsonify({"message": f"Found {len(results)} student(s)", "results": results})


# --------------------------------------------------
# UPDATE - Update only the fields received from browser
# --------------------------------------------------
@app.route('/update', methods=['POST'])
def update():
    data       = request.get_json()
    student_id = data['id']

    # if/else — check if ID is provided
    if student_id == '':
        return jsonify({"message": "Student ID is required!"})

    # Build the update query with only the fields that were sent
    fields = []
    values = []

    if 'name' in data and data['name'] != '':
        fields.append('name = ?')
        values.append(data['name'])

    if 'email' in data and data['email'] != '':
        fields.append('email = ?')
        values.append(data['email'])

    if 'city' in data and data['city'] != '':
        fields.append('city = ?')
        values.append(data['city'])

    # if/else — check if any field was given
    if len(fields) == 0:
        return jsonify({"message": "No fields to update!"})

    values.append(student_id)
    query = 'UPDATE students SET ' + ', '.join(fields) + ' WHERE id = ?'

    conn = sqlite3.connect('students.db')
    cursor = conn.execute(query, values)
    conn.commit()
    conn.close()

    # if/else — check if the student ID actually existed
    if cursor.rowcount == 0:
        return jsonify({"message": f"No student found with ID {student_id}!"})
    else:
        print(f"Updated ID {student_id} — fields: {fields}")
        return jsonify({"message": f"Student ID {student_id} updated successfully!"})


# --------------------------------------------------
# DELETE - Delete a student by ID
# --------------------------------------------------
@app.route('/delete', methods=['POST'])
def delete():
    data       = request.get_json()
    student_id = data['id']

    # if/else — check if ID is provided
    if student_id == '':
        return jsonify({"message": "Student ID is required!"})

    conn = sqlite3.connect('students.db')
    cursor = conn.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()

    # if/else — check if the student ID actually existed
    if cursor.rowcount == 0:
        return jsonify({"message": f"No student found with ID {student_id}!"})
    else:
        print(f"Deleted ID {student_id}")
        return jsonify({"message": f"Student ID {student_id} deleted successfully!"})


# --------------------------------------------------
# Start the app
# --------------------------------------------------
if __name__ == '__main__':
    create_database()
    app.run(debug=True)
