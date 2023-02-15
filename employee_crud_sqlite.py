import sqlite3

from flask import Flask, jsonify, request, g, render_template

app = Flask(__name__)
DATABASE = 'employees.db'

# Create a connection to the database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Create the employee table
def create_table():
    db = get_db()
    db.execute('CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, department TEXT)')

# Insert a new employee record
def insert_employee(name, age, department):
    db = get_db()
    db.execute('INSERT INTO employees (name, age, department) VALUES (?, ?, ?)', (name, age, department))
    db.commit()

# Retrieve all employee records
def get_all_employees():
    db = get_db()
    cursor = db.execute('SELECT id, name, age, department FROM employees')
    employees = [{'id': row[0], 'name': row[1], 'age': row[2], 'department': row[3]} for row in cursor.fetchall()]
    return employees

# Retrieve a specific employee record
def get_employee(id):
    db = get_db()
    cursor = db.execute('SELECT id, name, age, department FROM employees WHERE id = ?', (id,))
    employee = cursor.fetchone()
    if employee is not None:
        return {'id': employee[0], 'name': employee[1], 'age': employee[2], 'department': employee[3]}
    else:
        return None

# Update an employee record
def update_employee(id, name, age, department):
    db = get_db()
    db.execute('UPDATE employees SET name = ?, age = ?, department = ? WHERE id = ?', (name, age, department, id))
    db.commit()

# Delete an employee record
def delete_employee(id):
    db = get_db()
    db.execute('DELETE FROM employees WHERE id = ?', (id,))
    db.commit()

# Define the endpoints
@app.route('/employees', methods=['GET'])
def get_employees():
    employees = get_all_employees()
    return jsonify(employees)

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id):
    employee = get_employee(id)
    if employee is not None:
        return jsonify(employee)
    else:
        return jsonify({'error': 'Employee not found'}), 404

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee_by_id(id):
    employee = get_employee(id)
    if employee is not None:
        name = request.json.get('name', employee['name'])
        age = request.json.get('age', employee['age'])
        department = request.json.get('department', employee['department'])
        update_employee(id, name, age, department)
        return '', 204
    else:
        return jsonify({'error': 'Employee not found'}), 404

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee_by_id(id):
    employee = get_employee(id)
    if employee is not None:
        delete_employee(id)
        return '', 204
    else:
        return jsonify({'error': 'Employee not found'}), 404

if __name__ == "__main__":
    app.run()