from models.student import Student
from models.course import Course
from models.teacher import Teacher
import json
from pathlib import Path
from utils.logging import log_error

def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
        
    except (FileNotFoundError, json.JSONDecodeError, PermissionError) as e:
        log_error(e)
        return []

def save_students(path, students):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    students_data = [
        {
            "student_id": student.student_id,
            "name": student.name,
            "age": student.age,
            "enrolled_courses": student.enrolled_courses
        }
        for student in students.values()
    ]

    with open(path, "w", encoding="utf-8") as file:
        json.dump(students_data, file, indent=4)

def save_courses(path, courses):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    courses_data = [
        {
            "course_code": course.course_code,
            "course_title": course.course_title,
            "assigned_teacher": course.assigned_teacher,
            "enrolled_students": course.enrolled_students
        }
        for course in courses.values()
    ]

    with open(path, "w", encoding="utf-8") as file:
        json.dump(courses_data, file, indent=4)

def save_teachers(path, teachers):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    teachers_data = [
        {
            "teacher_id": teacher.teacher_id,
            "name": teacher.name,
            "subject": teacher.subject
        }
        for teacher in teachers.values()
    ]

    with open(path, "w", encoding="utf-8") as file:
        json.dump(teachers_data, file, indent=4)

def load_students(path):
    students_data = load_json(path)
    students = {}

    try:
        for student_data in students_data:
            student = Student(
                student_data["student_id"],
                student_data["name"],
                student_data["age"]
            )

            student.enrolled_courses = student_data["enrolled_courses"]
            students[student.student_id] = student

    except (KeyError, ValueError) as e:
        log_error(e)
        return {}

    return students

def load_courses(path):
    courses_data = load_json(path)
    courses = {}

    try:
        for course_data in courses_data:
            course = Course(
                course_data["course_code"],
                course_data["course_title"],
                course_data["assigned_teacher"]
            )

            course.enrolled_students = course_data["enrolled_students"]
            courses[course.course_code] = course

    except (KeyError, ValueError) as e:
        log_error(e)
        return {}

    return courses

def load_teachers(path):
    teachers_data = load_json(path)
    teachers = {}

    try:
        for teacher_data in teachers_data:
            teacher = Teacher(
                teacher_data["teacher_id"],
                teacher_data["name"],
                teacher_data["subject"]
            )

            teachers[teacher.teacher_id] = teacher

    except (KeyError, ValueError) as e:
        log_error(e)
        return {}

    return teachers