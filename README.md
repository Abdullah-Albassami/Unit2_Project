# School Management System

A Python command-line School Management System built using object-oriented programming, file handling, JSON persistence, validation, and exception handling.

## Features

- Add students
- Add courses
- Add teachers
- Enroll students in courses
- Drop students from courses
- Assign teachers to courses
- View students and their enrolled courses
- View courses and their enrolled students
- Save and load data using JSON
- Validate user input
- Handle invalid operations using custom exceptions
- Log errors to `logs.txt`

## Project Structure

```text
Unit2_Project/
├── .gitignore
├── README.md
└── school_system/
    ├── main.py
    ├── logs.txt
    ├── data/
    │   ├── students.json
    │   ├── courses.json
    │   └── teachers.json
    ├── models/
    │   ├── student.py
    │   ├── course.py
    │   ├── teacher.py
    │   └── school.py
    └── utils/
        ├── validators.py
        ├── exceptions.py
        ├── file_handler.py
        └── logging.py
```

## How to Run

From the `Unit2_Project` directory:

```bash
cd school_system
python3 main.py
```

## Concepts Used

- Classes and objects
- Object-oriented programming
- Lists and dictionaries
- Modules and imports
- Input validation
- Custom exceptions
- Exception handling
- JSON file handling
- `pathlib`
- Error logging
