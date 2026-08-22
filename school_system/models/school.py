from utils.validators import validate_id
from utils.exceptions import (
    StudentNotFoundError, CourseNotFoundError, TeacherNotFoundError, 
    StudentAlreadyExistsError, CourseAlreadyExistsError, TeacherAlreadyExistsError
    )

class School:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.teachers = {}

    def add_student(self, student):
        if student.student_id in self.students:
            raise StudentAlreadyExistsError

        self.students[student.student_id] = student

    def add_course(self, course):
        if course.course_code in self.courses:
            raise CourseAlreadyExistsError

        self.courses[course.course_code] = course

    def add_teacher(self, teacher):
        if teacher.teacher_id in self.teachers:
            raise TeacherAlreadyExistsError

        self.teachers[teacher.teacher_id] = teacher

    def enroll_student(self, student_id, course_code):
        student_id = validate_id(student_id)
        course_code = validate_id(course_code)

        if student_id not in self.students:
            raise StudentNotFoundError

        if course_code not in self.courses:
            raise CourseNotFoundError

        student = self.students[student_id]
        course = self.courses[course_code]

        student.enroll_in_course(course_code)
        course.add_student(student_id)

    def drop_student(self, student_id, course_code):
        student_id = validate_id(student_id)
        course_code = validate_id(course_code)

        if student_id not in self.students:
            raise StudentNotFoundError

        if course_code not in self.courses:
            raise CourseNotFoundError

        student = self.students[student_id]
        course = self.courses[course_code]

        student.drop_course(course_code)
        course.remove_student(student_id)

    def display_students(self):
        if not self.students:
            return ["No students found."]
        
        view_students = []
        for student in self.students.values():
            course_titles = [
                self.courses[course_code].course_title
                for course_code in student.enrolled_courses
                if course_code in self.courses
            ]

            view_students.append(
                student.view_student_info(course_titles)
            )
        return view_students

    def display_courses(self):
        if not self.courses:
            return ["No courses found."]

        view_courses = [
            course.display_course_info()
            for course in self.courses.values()
        ]

        return view_courses

    def view_student_courses(self, student_id):
        student_id = validate_id(student_id)

        if student_id not in self.students:
            raise StudentNotFoundError

        student = self.students[student_id]

        course_titles = [
            self.courses[course_code].course_title
            for course_code in student.enrolled_courses
            if course_code in self.courses
        ]

        if not course_titles:
            return "No courses enrolled."

        return f"Courses: {', '.join(course_titles)}"

    def view_course_students(self, course_code):
        course_code = validate_id(course_code)
        if course_code not in self.courses:
            raise CourseNotFoundError

        course = self.courses[course_code]
        if not course.enrolled_students:
            return "No students enrolled."

        return f"Students: {', '.join(course.enrolled_students)}"

    def assign_teacher(self, teacher_id, course_code):
        teacher_id = validate_id(teacher_id)
        course_code = validate_id(course_code)

        if teacher_id not in self.teachers:
            raise TeacherNotFoundError

        if course_code not in self.courses:
            raise CourseNotFoundError

        self.courses[course_code].assigned_teacher = teacher_id