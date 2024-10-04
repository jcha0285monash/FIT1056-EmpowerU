"""
FIT1056 2024 Semester 2
Programming Concepts Task 4

This file contains the class definition for the ReceptionistUser class.
"""

# Standard library imports
import os

# Local application imports
from app.pst4_app_user import User
# from app.pst4_app_student import StudentUser
from app.pst4_app_teacher import TeacherUser

class ReceptionistUser(User):

    @staticmethod
    def authenticate(input_username, input_password):
        """
        Method to authenticate a ReceptionistUser user.

        Parameter(s):
        - input_username: str
        - input_password: str

        Returns:
        - an instance of ReceptionistUser corresponding to the username if successful,
          None otherwise
        """
        recept_path = "./data/pst4_receptionists.txt"
        if os.path.exists(recept_path):
            with open(recept_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                # Sequence unpacking: 
                # https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
                recept_id, first_name, last_name, contact_num, username, password = line.strip("\n").split(",")
                
                if input_username == username:
                    if input_password == password:
                        return ReceptionistUser(recept_id, first_name, last_name, contact_num, input_username, input_password)
                    else:
                        return None # or return, or break
        else:
            print(f"Please check subdirectory and file {recept_path} exists.")
        

    def __init__(self, uid, first_name, last_name, contact_num, username, password):
        """
        Constructor method for the ReceptionistUser class
        """
        super().__init__(uid, first_name, last_name, contact_num)
        self.username = username
        self.password = password
        self.import_all_data()

    def import_all_data(self):
        """
        Method to read all data by calling methods to read teachers data and students data.

        Parameter(s):
        (None)

        Returns:
        (None)
        """
        self.import_teachers_data()
        # self.import_students_data()

    def import_teachers_data(self):
        """
        Method to read teachers data and store it into the receptionist's session.

        Parameter(s):
        (None)

        Returns:
        (None)
        """
        self.teachers = []
        teachers_path = "./data/pst4_teachers.txt"
        if os.path.exists(teachers_path):
            with open(teachers_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                # Sequence unpacking
                # https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
                teacher_id, first_name, last_name, contact_num, instruments = line.strip("\n").split(",")
                instruments_list = instruments.split("&")
                teacher_obj = TeacherUser(teacher_id, first_name, last_name, contact_num, instruments_list)
                self.teachers.append(teacher_obj)
        else:
            print(f"Please check the subdirectory and file exists for {teachers_path}.")

    # def import_students_data(self):
    #     """
    #     Method to read students data and store it into the receptionist's session.

    #     Parameter(s):
    #     (None)

    #     Returns:
    #     (None)
    #     """
    #     self.students = []
    #     students_path = "./data/pst4_students.txt"
    #     if os.path.exists(students_path):
    #         with open(students_path, "r", encoding="utf8") as rf:
    #             lines = rf.readlines()
    #         for line in lines:
    #             student_id, first_name, last_name, date_of_birth, contact_name, contact_num = line.strip("\n").split(",")
    #             student_obj = StudentUser(student_id, first_name, last_name, date_of_birth, contact_name, contact_num)
    #             self.students.append(student_obj)
    #     else:
    #         print(f"Please check the subdirectory and file exists for {students_path}.")


    def list_teachers_by_instrument(self, instrument):
        """
        This method retrieves Teachers that are qualified to teach the specified instrument

        Parameter(s):
        - instrument: str, the instrument to be searched
        
        Returns:
        - list: list of Teacher objects that match the criteria
        """
        results = []
        for teacher_obj in self.teachers:
            if instrument.title() in teacher_obj.instruments:
                results.append(teacher_obj)
                continue

        return results

    # def store_student_data(self, first_name, last_name, date_of_birth, contact_name, contact_num):
    #     """
    #     Method to register the student in the system 
    #     and write the data of the new student into the file.

    #     Parameter(s):
    #     - first_name: str, student's first name
    #     - last_name: str, student's last name
    #     - date_of_birth: str, student's date of birth
    #     - contact_name: str, name of student's contact person
    #     - contact_num: str, contact number of either student or contact person

    #     Returns:
    #     - bool: True if student data is stored from the system into the txt file, 
    #             False otherwise
    #     """

    #     # Create the Student object
    #     # Assume no skips in student ID
    #     student_id = "s" + str(len(self.students) + 1).zfill(4)
    #     student_obj = StudentUser(student_id, first_name, last_name, date_of_birth, contact_name, contact_num)
    #     self.students.append(student_obj)

    #     # Write to ./data/pst4_students.txt in a comma-separated format
    #     filepath = "./data/pst4_students.txt"
    #     if os.path.exists(filepath):
    #         with open(filepath, "a", encoding="utf8") as f:
    #             new_student_line = f"{student_id},{first_name},{last_name},{date_of_birth},{contact_name},{contact_num}"
    #             f.write(new_student_line + "\n")
    #         return True
    #     else:
    #         print(f"Please check the subdirectory and file {filepath} exists!")
    #         return False

    # def store_class_data(self, day_of_week, start_time, duration_minutes):
    #     """
    #     This method creates a class that is held weekly.

    #     Parameters:
    #     - day_of_week: str, name of the day of the week (e.g. Monday, Tuesday, etc.)
    #     - start_time: str, in HH:mm format (e.g. 08:00)
    #     - duration_minutes: int, number of minutes

    #     Returns:
    #     - bool: True if class data is stored from the system into the txt file, 
    #             False otherwise
    #     """

    #     # Write to pst4_classes.txt in a comma-separated format
    #     filepath = "./data/pst4_classes.txt"
    #     if os.path.exists(filepath):
    #         with open(filepath, "a", encoding="utf8") as f:
    #             new_class_line = f"{day_of_week},{start_time},{duration_minutes}"
    #             f.write(new_class_line + "\n")
    #         return True
    #     else:
    #         print(f"Please check the subdirectory and file {filepath} exists!")
    #         return False

if __name__ == "__main__":
    pass
