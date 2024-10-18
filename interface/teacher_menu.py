import tkinter as tk
from interface.teacher_menus.teacher_courses_menu import TeacherCoursesMenu
from interface.teacher_menus.teacher_student_menu import TeacherStudentMenu

class TeacherMenu(tk.Frame):
    def __init__(self, master, teacher_user):
        super().__init__(master)
        self.master = master        
        self.teacher_user = teacher_user

        #teacher heading
        self.teacher_heading = tk.Label(self, text="Teacher Menu", font=("Arial", 16))
        self.teacher_heading.pack(pady=20)

        # View all students button
        self.view_students_button = tk.Button(self, text="View All Students", command=self.view_students_button_clicked)
        self.view_students_button.pack(pady=10)

        # View all courses button
        self.view_courses_button = tk.Button(self, text="View All Courses", command=self.view_courses_button_clicked)
        self.view_courses_button.pack(pady=10)

        #logout button
        self.logout_button = tk.Button(self, text="Logout", command=self.logout_button_clicked)
        self.logout_button.pack(pady=10)

    def show_menu(self):
        self.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    def view_students_button_clicked(self):
        self.master.hide_teacher_menu(self)
        student_menu = TeacherStudentMenu(self.master,self.teacher_user, self)
        student_menu.pack(fill="both", expand=True)

    def view_courses_button_clicked(self):
        self.master.hide_teacher_menu(self)
        teacher_courses_menu = TeacherCoursesMenu(self.master, self.teacher_user, self)
        teacher_courses_menu.pack(fill="both", expand=True)

    def logout_button_clicked(self):
        self.master.hide_teacher_menu(self)
        self.master.show_homepage()