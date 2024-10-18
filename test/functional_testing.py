import pytest 
from app import user, student, teacher, staff

def test_authenticate():
    test_authenticate = student.authenticate("stu123", "password123")
    assert test_authenticate == None
    test_authenticate = teacher.authenticate("tea123", "password123")
    assert test_authenticate == None