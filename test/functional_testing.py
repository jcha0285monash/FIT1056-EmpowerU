import sys
sys.path.append("..")
import pytest
from app.staff import Staff
from app.student import Student
from app.teacher import Teacher

def test_authenticate():
    
    # try logging on with incorrect credentials
    test_authenticate = Student.authenticate("stu123", "password123")
    assert test_authenticate == None
    test_authenticate = Teacher.authenticate("tea123", "password123")
    assert test_authenticate == None
    test_authenticate = Staff.authenticate("sta123", "password123")