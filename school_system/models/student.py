from utils.validators import validate_name, validate_age, validate_id
from utils.exceptions import AlreadyEnrolledError, NotEnrolledError

class Student:
    def __init__(self, student_id, name, age):
        self.student_id = validate_id(student_id)
        self.name = validate_name(name)
        self.age = validate_age(age)
        self.enrolled_courses = []

    def enroll_in_course(self, course_code):
        course_code = validate_id(course_code)

        if course_code in self.enrolled_courses:
            raise AlreadyEnrolledError

        self.enrolled_courses.append(course_code)

    def drop_course(self, course_code):
        course_code = validate_id(course_code)

        if course_code not in self.enrolled_courses:
            raise NotEnrolledError

        self.enrolled_courses.remove(course_code)

    def view_student_info(self, course_titles):
        return (
            f"{self.student_id} | {self.name} | Age {self.age}\n"
            f"Courses: {', '.join(course_titles)}"
        )