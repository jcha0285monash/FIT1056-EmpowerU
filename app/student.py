from app.user import User
import os

class Student:
    def __init__(self, uid, email, password, name, course, status):
        self.uid = uid
        self.email = email
        self.password = password
        self.name = name
        self.course = course
        self.status = status

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

    @staticmethod
    def import_students(filepath=".."):
        students = []
        student_path = f"{filepath}/database/student.txt"
        if os.path.exists(student_path):
            with open(student_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                stu_id, email, password, name, course, status = line.strip().split(",")
                student_obj = Student(stu_id, email, password, name, course, status)
                students.append(student_obj)
        return students

    @staticmethod
    def register_student(name, email, password, course="", status="ACTIVE"):
        if Student.validate_email(email) == False:
            students = Student.import_students()
            student_path = "./database/student.txt"
            stu_id = "stu" + str(len(students) + 1).zfill(4)
            new_student = Student(stu_id, email, password, name, course, status)
            students.append(new_student)
            
            if os.path.exists(student_path):
                with open(student_path, "a", encoding="utf8") as f:
                    student_data = f"{stu_id},{email},{password},{name},{course},{status}"
                    f.write(student_data + "\n")
            
            return new_student
        else  :
            return None

    @staticmethod
    def validate_email(email):
        students = Student.import_students()
        for student in students:
            if student.email == email:
                return True
        return False