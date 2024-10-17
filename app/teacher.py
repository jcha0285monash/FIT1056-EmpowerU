from app.user import User
import os

class Teacher(User):
    @staticmethod
    def authenticate(uid, password):
        teacher_path = "./database/teacher.txt"
        if os.path.exists(teacher_path):
            with open(teacher_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                tea_id, email, stored_password, name, course, status = line.strip().split(",")
                if uid == tea_id and password == stored_password and status != "DEACTIVATED":
                    if "tea" in tea_id.lower():
                        return Teacher(tea_id, email, password, name, course, status)
                    else:
                        return None
                    
    def __init__(self, uid, email, password, name, course, status):
        super().__init__(uid, email, name, password, status)
        self.course = course
