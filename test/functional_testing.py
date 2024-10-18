import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.user import User
from app.student import Student
from app.staff import Staff
from app.teacher import Teacher
import pytest

def test_authenticate():
    # try logging on with correct credentials
    test_authenticate = Student.authenticate("stu0001", "pass")
    assert type(test_authenticate) == Student
    assert test_authenticate.name == "Joel"
    assert test_authenticate.email == "joel@monash.edu"
    
    # try logging on with incorrect credentials
    test_authenticate = Student.authenticate("stu123", "password123")
    assert test_authenticate == None
    test_authenticate = Teacher.authenticate("tea123", "password123")
    assert test_authenticate == None
    test_authenticate = Staff.authenticate("sta123", "password123")
    assert test_authenticate == None
    