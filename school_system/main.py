from models.student import Student
from models.course import Course
from models.teacher import Teacher
from models.school import School
from utils.logging import log_error
from utils.file_handler import (
    load_students, load_courses, load_teachers, 
    save_students, save_courses, save_teachers
    )
from utils.exceptions import (
    StudentNotFoundError, CourseNotFoundError, TeacherNotFoundError, StudentAlreadyExistsError,
    CourseAlreadyExistsError, TeacherAlreadyExistsError, AlreadyEnrolledError, NotEnrolledError
    )

STUDENTS_FILE = "data/students.json"
COURSES_FILE = "data/courses.json"
TEACHERS_FILE = "data/teachers.json"

school = School()

school.students = load_students(STUDENTS_FILE)
school.courses = load_courses(COURSES_FILE)
school.teachers = load_teachers(TEACHERS_FILE)

while True:
    print("\nSCHOOL MANAGEMENT SYSTEM")
    print("1. Add student")
    print("2. Add course")
    print("3. Add teacher")
    print("4. Enroll student")
    print("5. Drop course")
    print("6. View students")
    print("7. View courses")
    print("8. View student courses")
    print("9. View course students")
    print("10. Assign teacher")
    print("11. Save and Exit")

    choice = input("Choose an option: ").strip()
    
    try:
        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            student = Student(student_id, name, age)
            school.add_student(student)
        elif choice == "2":
            course_code = input("Enter course code: ")
            course_title = input("Enter course title: ")
            course = Course(course_code, course_title)
            school.add_course(course)

        elif choice == "3":
            teacher_id = input("Enter teacher ID: ")
            name = input("Enter teacher name: ")
            subject = input("Enter subject: ")
            teacher = Teacher(teacher_id, name, subject)
            school.add_teacher(teacher)

        elif choice == "4":
            student_id = input("Enter student ID: ")
            course_code = input("Enter course code: ")
            school.enroll_student(student_id, course_code)

        elif choice == "5":
            student_id = input("Enter student ID: ")
            course_code = input("Enter course code: ")
            school.drop_student(student_id, course_code)

        elif choice == "6":
            for student in school.display_students():
                print("\n", student, "\n")

        elif choice == "7":
            for course in school.display_courses():
                print("\n", course, "\n")

        elif choice == "8":
            student_id = input("Enter student ID: ")
            print(school.view_student_courses(student_id))

        elif choice == "9":
            course_code = input("Enter course code: ")
            print(school.view_course_students(course_code))

        elif choice == "10":
            teacher_id = input("Enter teacher ID: ")
            course_code = input("Enter course code: ")
            school.assign_teacher(teacher_id, course_code)

        elif choice == "11":
            save_students(STUDENTS_FILE, school.students)
            save_courses(COURSES_FILE, school.courses)
            save_teachers(TEACHERS_FILE, school.teachers)
            print("Data saved.")
            break

        else:
            print("Invalid option")

    except ValueError as error:
        print(f"Error: {error}") 
        log_error(error)
    except (
        StudentNotFoundError,
        CourseNotFoundError,
        TeacherNotFoundError,
        StudentAlreadyExistsError,
        CourseAlreadyExistsError,
        TeacherAlreadyExistsError,
        AlreadyEnrolledError,
        NotEnrolledError
    ) as error:
        print(f"Error: {error}")
        log_error(error)
        
    except (FileNotFoundError, PermissionError) as error:
        print(f"File error: {error}")
        log_error(error)
