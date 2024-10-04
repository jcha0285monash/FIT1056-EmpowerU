import tkinter as tk
from interface.available_courses_menu import AvailableCoursesMenu
from interface.current_courses_menu import CurrentCoursesMenu

class StudentMenu(tk.Frame):
    def __init__(self, master, student_user):
        super().__init__(master)
        self.master = master
        self.student_user = student_user

        #student heading
        self.student_heading = tk.Label(self, text=f"Welcome, {student_user.name}!", font=("Arial", 20))
        self.student_heading.pack(pady=20)

        #view available courses button
        self.view_available_courses_button = tk.Button(self, text="View Available Courses", command=self.view_available_courses_button_clicked)
        self.view_available_courses_button.pack(pady=10)

        # current courses heading
        self.heading = tk.Label(self, text="Current Courses", font=("Arial", 18, "bold"))
        self.heading.pack(pady=20)

        # current courses list
        self.courses_list = tk.Listbox(self, width=50, height=10)
        self.courses_list.pack(pady=20)
        self.load_courses()

        # alert variable and label widget
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(self, textvariable=self.alert_var, fg="red", font=("Arial", 12))
        self.alert_label.pack(pady=10)

        #logout button
        self.logout_button = tk.Button(self, text="Logout", command=self.logout_button_clicked)
        self.logout_button.pack(pady=10)

    def load_courses(self):
        self.courses_list.delete(0, tk.END)
        current_courses = self.student_user.course.split("&")
        for courses in current_courses:
            if courses != "":
                self.courses_list.insert(tk.END, courses)

    def logout_button_clicked(self):
        self.master.hide_student_menu(self)
        self.master.show_homepage()

    def view_available_courses_button_clicked(self):
        self.master.hide_student_menu(self)
        available_courses_menu = AvailableCoursesMenu(self.master, self.student_user, self)
        self.master.show_available_courses_menu(available_courses_menu)