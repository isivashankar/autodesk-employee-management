import sqlite3

def create_database():
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, department TEXT)''')
    conn.commit()
    conn.close()

def add_employee(id, name,age, department):
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute("INSERT INTO employees (id, name, age, department) VALUES (?, ?, ?, ?)", (id, name, age, department))
    conn.commit()
    conn.close()

def get_employees():
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute("SELECT * FROM employees")
    employees = c.fetchall()
    conn.close()
    return employees

def update_employee(id, name=None, age=None, department=None):
    conn = sqlite3.connect('employees.db')
    
    c = conn.cursor()
    c.execute('UPDATE employees SET name = ?, age = ?, department = ? WHERE id = ?', (name, age, department, id))
    conn.commit()
    conn.close()

def delete_employee(id):
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute("DELETE FROM employees WHERE id = ?", (id,))
    conn.commit()
    conn.close()

create_database()
# Add some employees
add_employee(1, "Aarav", 25, "HR")
add_employee(2, "Aditya", 30, "Sales")
add_employee(3, "Advait", 28, "Marketing")
add_employee(4, "Ananya", 27, "IT")
add_employee(5, "Arya", 26, "HR")
add_employee(6, "Atharv", 24, "Sales")
add_employee(7, "Avi", 31, "Marketing")
add_employee(8, "Dia", 29, "IT")
add_employee(9, "Isha", 32, "HR")
add_employee(10, "Kavya", 33, "Sales")
add_employee(11, "Manan", 26, "Marketing")
add_employee(12, "Neha", 28, "IT")

# Get all employees
employees = get_employees()
for employee in employees:
    print(employee)

# Update an employee
update_employee(1, name="John Smith", age=34)

# Delete an employee
delete_employee(2)
