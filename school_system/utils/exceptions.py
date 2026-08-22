class StudentNotFoundError(Exception):
    def __init__(self, message="Student ID does not exist"):
        super().__init__(message)

class CourseNotFoundError(Exception):
    def __init__(self, message="Course code does not exist"):
        super().__init__(message)

class TeacherNotFoundError(Exception):
    def __init__(self, message="Teacher ID does not exist"):
        super().__init__(message)

class StudentAlreadyExistsError(Exception):
    def __init__(self, message="Student ID already exists"):
        super().__init__(message)

class CourseAlreadyExistsError(Exception):
    def __init__(self, message="Course code already exists"):
        super().__init__(message)

class TeacherAlreadyExistsError(Exception):
    def __init__(self, message="Teacher ID already exists"):
        super().__init__(message)

class AlreadyEnrolledError(Exception):
    def __init__(self, message="Student is already enrolled in this course"):
        super().__init__(message)

class NotEnrolledError(Exception):
    def __init__(self, message="Student is not enrolled in this course"):
        super().__init__(message)