import tkinter as tk
import os

class StaffCoursesMenu(tk.Frame):
    def __init__(self, master, staff_user, staff_menu):
        super().__init__(master)
        self.master = master
        self.staff_user = staff_user
        self.staff_menu = staff_menu

        # all courses heading
        self.heading = tk.Label(self, text="All Courses", font=("Arial", 18, "bold"))
        self.heading.pack(pady=20)

        # all courses listbox
        self.courses_listbox = tk.Listbox(self, width=50, height=10)
        self.courses_listbox.pack(pady=20)
        self.load_courses()

        # alert variable and label widget
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(self, textvariable=self.alert_var, font=("Arial", 12))
        self.alert_label.pack(pady=10)

        # edit course button
        self.select_course_button = tk.Button(self, text="Edit Course", command=self.edit_course_button_clicked)
        self.select_course_button.pack(pady=20)

        # back to home button
        self.back_to_home_button = tk.Button(self, text="Back to Home", command=self.back_to_home_button_clicked)
        self.back_to_home_button.pack(pady=10)

    def edit_course_button_clicked(self):
        # todo
        pass

    def load_courses(self):
        self.courses_listbox.delete(0, tk.END)
        available_courses_path = "database/available_courses.txt"
        if os.path.exists(available_courses_path):
            with open(available_courses_path, "r", encoding="utf-8") as rf:
                lines = rf.readlines()
            for line in lines:
                self.courses_listbox.insert(tk.END, line.strip())
            
    def back_to_home_button_clicked(self):
        self.master.hide_staff_staff_menu(self)
        self.master.show_staff_menu(self.staff_menu)
