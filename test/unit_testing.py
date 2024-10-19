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

# ** Test if students can be imported
def test_import_students():
    students = Student.import_students()
    assert len(students) > 0
    for student in students:
        assert isinstance(student, Student)
        assert student.uid.startswith("stu")
        
#* Positive Testing for different user's authentication
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
   
    
#* Positive Testing for registration as a normal user
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
                
#* Positive Testing for staff to create teachers
def test_create_teacher():
    user_path = "./database/teacher.txt"
    test_create_teacher = Staff.add_user("tea123", "Johnathan", "Johnathan@EmpowerU.com", "pass", user_path, "Programming in Python")
    teacher_data = test_create_teacher.split(",")
    teacher = Teacher(*teacher_data)
    assert isinstance(teacher, Teacher)
    assert teacher.uid == "tea123"
    assert teacher.email == "Johnathan@EmpowerU.com"
    assert teacher.name == "Johnathan"
    assert teacher.course == "Programming in Python"
    
    
#* Positive Testing for editing a user's details
def test_edit_user():
    user_path = "./database/staff.txt"
    test_edit_user = Staff.edit_user("sta2", "editedEmail@gmail.com", "2", "Eddy", "staff" ,user_path, selected_line=1, selected_user_status="ACTIVE") 
    edited_user = test_edit_user.split(",")
    user = Staff(*edited_user)
    assert isinstance(user, Staff)
    assert user.uid == "sta2"
    assert user.email == "editedEmail@gmail.com"
    assert user.name == "Eddy"
