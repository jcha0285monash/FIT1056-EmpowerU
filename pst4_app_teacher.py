"""
FIT1056 2024 Semester 2
Programming Concepts Task 4

This file contains the class definition for the TeacherUser class.
"""

# Local application imports
from app.pst4_app_user import User

class TeacherUser(User):

    def __init__(self, uid, first_name, last_name, contact_num, instruments):
        """
        Constructor for the TeacherUser class
        """
        super().__init__(uid, first_name, last_name, contact_num)
        self.instruments = instruments


if __name__ == "__main__":
    pass