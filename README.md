# Student Record System

A simple command-line based Student Record Management System built with Python. This project allows users to store, manage, and manipulate student records using Python dictionaries and lists.

## Features

* Add new student records
* Search for a student by ID
* Display all student records
* Update a student's department
* Delete a student record
* Find the student with the highest GPA

## Technologies Used

* Python 3
* Lists
* Dictionaries
* Functions

## Project Structure

Each student record is stored as a dictionary with the following fields:

```python
{
    "ID": 17503,
    "NAME": "Nisa Nayab",
    "AGE": 20,
    "DEPARTMENT": "Data Science",
    "GPA": 4.0
}
```

All student records are maintained in a list named `students`.

## Functions

### `Add_Student(student_id, student_name, age, department, GPA)`

Adds a new student to the system.

### `searching_students(students, student_id)`

Searches for a student using their ID and displays their details.

### `displaying_students(students)`

Displays all student records.

### `deleting_student(students, student_id)`

Removes a student record from the system using their ID.

### `updating_student(students, student_id, new_department)`

Updates the department of an existing student.

### `highest_gpa(students)`

Finds and displays the student with the highest GPA.

## Example Usage

```python
Add_Student(17503, "Nisa Nayab", 20, "Data Science", 4.0)
Add_Student(17504, "Narin", 21, "Computer Science", 3.9)
Add_Student(17505, "Merjan", 24, "Cyber Security", 4.0)

displaying_students(students)

searching_students(students, 17503)

updating_student(students, 17505, "AI")

deleting_student(students, 17504)

highest_gpa(students)
```

## How to Run

1. Make sure Python 3 is installed on your system.
2. Save the code in a file named `student_record_system.py`.
3. Open a terminal in the project directory.
4. Run the following command:

```bash
python student_record_system.py
```

## Future Improvements

* Add input validation
* Prevent duplicate student IDs
* Store records in a file or database
* Create a menu-driven interface
* Add options to update age, GPA, and name
* Implement sorting and filtering features

## Author

Nisa Nayab

