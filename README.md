# Flask CRUD Service for Employee Records

This is a simple Flask-based CRUD service for managing employee records. The service exposes the following endpoints:

- `GET /employees` - Retrieves all employee records
- `GET /employees/{id}` - Retrieves a specific employee record by ID
- `PUT /employees/{id}` - Updates a specific employee record by ID
- `DELETE /employees/{id}` - Deletes a specific employee record by ID

## Setup and Configuration

This service requires a SQLite database to store employee records. The database connection is established and managed using Flask's `g` object. To configure the database connection, modify the `DATABASE` variable in `employee_crud_sqlite.py` to specify the path to the database file.

I have manually created employees.db using the `db_creation.py` file

## API Documentation

### GET /employees

Retrieves all employee records.

##### Request Parameters

None

##### Response

On success, returns a JSON object containing an array of employee records. Each employee record is represented as a JSON object with the following properties:

- `id` - The employee ID
- `name` - The employee name
- `age` - The employee age
- `department` - The employee department

##### Example Request
http://localhost:5000/employees


##### Example Response

```json
[
    {
        "id": 1,
        "name": "Aarav",
        "age": 23,
        "department": "Sales"
    },
    {
        "id": 2,
        "name": "Aditya",
        "age": 32,
        "department": "Marketing"
    },
    ...
    {
        "id": 12,
        "name": "Rahul",
        "age": 26,
        "department": "Support"
    }
]
```

### GET /employees/{id}
Retrieves a specific employee record by ID.

#### Request Parameters
id - The ID of the employee record to retrieve
#### Response
On success, returns a JSON object representing the requested employee record. The employee record is represented as per the given id

##### Example Request
http://localhost:5000/employees/2

##### Example Response
```json
{
    "id": 1,
    "name": "Rajesh",
    "age": 26,
    "department": "Engineering"
}
```


### PUT /employees/<id>

#### Request Parameters
id - The ID of the employee record to retrieve
#### Request body:

```json
{
    "name": "Raj",
    "age": 26,
    "department": "Engineering"
}
```
#### Response:

Returns an empty response with a status code of 204 (No Content).

### DELETE /employees/<id>
#### Request Parameters
id - The ID of the employee record to retrieve
#### Response:
Returns an empty response with a status code of 204 (No Content).

### Employee Record Structure
Each employee record in the database has the following structure:

The Employee record has the following fields:

- `id`: the unique identifier of the Employee record
- `name`: the name of the Employee
- `age`: the age of the Employee
- `department`: the department in which the Employee works


### Dependencies
This project requires the following dependencies:

- Python 3.x
- Flask
- SQLite3