import os
import sys
from unittest.mock import Mock
import tkinter as tk
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.user import User
from app.student import Student
from app.staff import Staff
from app.teacher import Teacher
from interface.staff_menus.staff_user_menu import StaffUserMenu
from interface.student_menu import StudentMenu

import pytest


#** Positive Testing for different user's authentication
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
    
    test_authenticate = Staff.authenticate("sta1", "1", "..")
    assert type(test_authenticate) == Staff
    assert test_authenticate.uid == "sta1"
    assert test_authenticate.name == "Emily"
    assert test_authenticate.email == "empowerustaff@gmail.com"
    assert test_authenticate.role == "staff&"
    assert test_authenticate.status == "ACTIVE"
    
    test_authenticate = Teacher.authenticate("tea1", "pass", "..")
    assert type(test_authenticate) == Teacher
    assert test_authenticate.uid == "tea1"
    assert test_authenticate.name == "Chloe"
    assert test_authenticate.email == "chloe@gmail.com"
    assert test_authenticate.status == "ACTIVE"
   
    
#** Positive Testing for registration
def test_student_registration():
    # Test valid registration
    reg_student = Student.register_student("Mark", "mark@gmail.com", "pass")
    assert isinstance(reg_student, Student)
    assert "stu" in reg_student.uid
    assert reg_student.name == "Mark"
    assert reg_student.email == "mark@gmail.com"
    
    reg_student = Student.register_student("Noah", "noah@gmail.com", "pass")
    assert isinstance(reg_student, Student)
    assert "stu" in reg_student.uid
    assert reg_student.name == "Noah"
    assert reg_student.email == "noah@gmail.com"
                

def test_create_teacher():
    # Create a real Tkinter root widget
    root = tk.Tk()
    # Create mock objects for the other required arguments
    staff_user = Mock()
    staff_menu = Mock()
    user = "teacher"  # Set the user type to 'teacher'
    
    # Create an instance of StaffUserMenu with the real Tkinter root and mock arguments
    staff_menu_instance = StaffUserMenu(root, staff_user, staff_menu, user)
    staff_menu_instance.user_path = f"./database/{staff_menu_instance.user}.txt"
    
    # Ensure the file exists before calling add_user, (https://www.geeksforgeeks.org/python-os-makedirs-method/), (https://bugs.python.org/issue33968)
    os.makedirs(os.path.dirname(staff_menu_instance.user_path), exist_ok=True)
    with open(staff_menu_instance.user_path, "a", encoding="utf8"):
        pass

    # Call the add_user method
    teacher_data = staff_menu_instance.add_user("tea123", "Johnathan", "Johnathan@EmpowerU.com", "pass", "Programming in Python", "ACTIVE")
    teacher_info = teacher_data.split(",")
    # * is used to unpack the list into arguments
    teacher = Teacher(*teacher_info)

    # Assertions to verify the teacher object
    assert isinstance(teacher, Teacher)
    assert teacher.uid == "tea123"
    assert teacher.email == "Johnathan@EmpowerU.com"
    assert teacher.name == "Johnathan"
    assert teacher.course == "Programming in Python"
    assert teacher.status == "ACTIVE"
    

# ** Test if students can be imported
def test_import_students():
    students = Student.import_students()
    assert len(students) > 0
    for student in students:
        assert isinstance(student, Student)
        assert student.uid.startswith("stu")