from app.user import User
import os

class Student(User):
    @staticmethod
    def authenticate(uid, password, filepath):
        student_path = f"{filepath}/database/student.txt"
        if os.path.exists(student_path):
            with open(student_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                stu_id, email, stored_password, name, course, status = line.strip().split(",")
                
                if course == None:
                    course = None
                    
                if uid == stu_id and password == stored_password and status == "ACTIVE":
                    if "stu" in stu_id.lower():
                        return Student(stu_id, email, password, name, course, status)
                    else:
                        return None

    def __init__(self, uid, email, password, name, course, status):
        super().__init__(uid, email, password, name, status)
        self.course = course