import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.user import User
from app.student import Student
from app.staff import Staff
from app.teacher import Teacher
from interface.student_menu import StudentMenu
import pytest

# Positive Testing for each respective unit

def test_authenticate():
    """
    This test will check if the respective users can login successfully,
    and the system will return the correct attributes of the user.
    """
    test_authenticate = Student.authenticate("stu0001", "pass", "..")
    assert type(test_authenticate) == Student
    assert test_authenticate.uid == "stu0001"
    assert test_authenticate.name == "Joel"
    assert test_authenticate.email == "joel@monash.edu"
    assert test_authenticate.status == "ACTIVE"
    
    test_authenticate = Staff.authenticate("sta1", "pass", "..")
    assert type(test_authenticate) == Staff
    assert test_authenticate.uid == "sta1"
    assert test_authenticate.name == "Emily"
    assert test_authenticate.email == "empowerustaff@gmail.com"
    assert test_authenticate.role == "staff"
    assert test_authenticate.status == "ACTIVE"
    
    test_authenticate = Teacher.authenticate("tea1", "pass", "..")
    assert type(test_authenticate) == Teacher
    assert test_authenticate.uid == "tea1"
    assert test_authenticate.name == "Chloe"
    assert test_authenticate.email == "chloe@gmail.com"
    assert test_authenticate.status == "ACTIVE"
    
    test_load_courses = StudentMenu.load_courses(StudentMenu, Student.authenticate("stu0001", "pass",".."))
    assert type(test_load_courses) == list
    for course in test_load_courses:
        assert type(course) == str
    assert "Programming in Python" in test_load_courses
    assert "Introduction to Information Security" in test_load_courses
    assert "Artificial Intelligence" in test_load_courses
   
test_authenticate()    
"""
def login_button_clicked(self):
# Get the entered UID and password
uid = self.uid_var.get()
password = self.password_var.get()

if "stu" in uid:
    # If the entered UID is a student, create a Student object and call the login method
    student_user = Student.authenticate(uid, password, ".")
    if isinstance(student_user, Student):
        # If the entered UID is a student, call the student_home method
        self.master.hide_homepage()
        studentmenu = StudentMenu(self.master, student_user)
        self.master.show_student_menu(studentmenu)
        self.clear_input()
"""