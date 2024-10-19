import tkinter as tk
from interface.staff_menus.staff_courses_menu import StaffCoursesMenu
from interface.staff_menus.staff_user_menu import StaffUserMenu

class StaffMenu(tk.Frame):
    def __init__(self, master, staff_user):
        super().__init__(master)
        self.master = master
        self.staff_user = staff_user

        # Staff Heading
        self.staff_heading = tk.Label(self, text=f"Welcome {staff_user.name}!", font=("Arial", 20, "bold"))
        self.staff_heading.pack(pady=20)

        # View all students button
        self.view_students_button = tk.Button(self, text="View All Students", command=self.view_students_button_clicked)
        self.view_students_button.pack(pady=10)

        # View all teachers button
        self.view_teachers_button = tk.Button(self, text="View All Teachers", command=self.view_teachers_button_clicked)
        self.view_teachers_button.pack(pady=10)

        # View all staff button
        self.view_staff_button = tk.Button(self, text="View All Staff", command=self.view_staff_button_clicked)
        self.view_staff_button.pack(pady=10)

        # View all courses button
        self.view_courses_button = tk.Button(self, text="View All Courses", command=self.view_courses_button_clicked)
        self.view_courses_button.pack(pady=10)

        #logout button
        self.logout_button = tk.Button(self, text="Logout", command=self.logout_button_clicked)
        self.logout_button.pack(pady=10)

    def view_students_button_clicked(self):
        self.master.hide_staff_menu(self)
        staff_user_menu = StaffUserMenu(self.master, self.staff_user, self, "student")
        self.master.show_staff_user_menu(staff_user_menu)

    def view_teachers_button_clicked(self):
        self.master.hide_staff_menu(self)
        staff_user_menu = StaffUserMenu(self.master, self.staff_user, self, "teacher")
        self.master.show_staff_user_menu(staff_user_menu)

    def view_staff_button_clicked(self):
        self.master.hide_staff_menu(self)
        staff_user_menu = StaffUserMenu(self.master, self.staff_user, self, "staff")
        self.master.show_staff_user_menu(staff_user_menu)

    def view_courses_button_clicked(self):
        self.master.hide_staff_menu(self)
        staff_courses_menu = StaffCoursesMenu(self.master, self.staff_user, self)
        self.master.show_staff_courses_menu(staff_courses_menu)

    def logout_button_clicked(self):
        self.master.hide_staff_menu(self)
        self.master.show_homepage()