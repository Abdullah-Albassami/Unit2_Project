from utils.validators import validate_name, validate_id

class Teacher:
    def __init__(self, teacher_id, name, subject):
        self.teacher_id = validate_id(teacher_id)
        self.name = validate_name(name)
        self.subject = validate_name(subject)

    def display_teacher_info(self):
        return (
            f"{self.teacher_id} | {self.name}\n"
            f"Subject: {self.subject}"
        )