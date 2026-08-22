from utils.validators import validate_name, validate_id
from utils.exceptions import AlreadyEnrolledError, NotEnrolledError

class Course:
    def __init__(self, course_code, course_title, assigned_teacher=None):
        self.course_code = validate_id(course_code)
        self.course_title = validate_name(course_title)
        self.assigned_teacher = assigned_teacher
        self.enrolled_students = []

    def add_student(self, student_id):
        student_id = validate_id(student_id)

        if student_id in self.enrolled_students:
            raise AlreadyEnrolledError

        self.enrolled_students.append(student_id)

    def remove_student(self, student_id):
        student_id = validate_id(student_id)

        if student_id not in self.enrolled_students:
            raise NotEnrolledError

        self.enrolled_students.remove(student_id)

    def display_course_info(self):
        return (
            f"{self.course_code} | {self.course_title}\n"
            f"Teacher: {self.assigned_teacher} | "
            f"Students: {', '.join(self.enrolled_students)}"
        )