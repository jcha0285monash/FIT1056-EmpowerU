from app.user import User
import os

class Student(User):
    @staticmethod
    def authenticate(uid, password):
        student_path = "./database/student.txt"
        if os.path.exists(student_path):
            with open(student_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                stu_id, email, stored_password, name, course = line.strip().split(",")
                if uid == stu_id and password == stored_password:
                    if "stu" in stu_id.lower():
                        return Student(stu_id, email, password, name, course)
                    else:
                        return None

    def __init__(self, uid, email, password, name, course):
        super().__init__(uid, email, password, name)
        self.course = course