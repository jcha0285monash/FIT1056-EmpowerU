import tkinter as tk
import os

class AvailableCoursesMenu(tk.Frame):
    def __init__(self, master, student_user, student_menu):
        super().__init__(master)
        self.master = master
        self.student_user = student_user
        self.student_menu = student_menu

        # available courses heading
        self.heading = tk.Label(self, text="Available Courses", font=("Arial", 18, "bold"))
        self.heading.pack(pady=20)

        # available courses listbox
        self.courses_listbox = tk.Listbox(self, width=50, height=10)
        self.courses_listbox.pack(pady=20)
        self.load_courses()

        # alert variable and label widget
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(self, textvariable=self.alert_var, font=("Arial", 12))
        self.alert_label.pack(pady=10)

        # select course button
        self.select_course_button = tk.Button(self, text="Select Course", command=self.select_course)
        self.select_course_button.pack(pady=20)

        # back to home button
        self.back_to_home_button = tk.Button(self, text="Back to Home", command=self.back_to_home_button_clicked)
        self.back_to_home_button.pack(pady=10)

    # select course and add it to the Student Class
    def select_course(self):
        selected_course = self.courses_listbox.get(tk.ACTIVE)
        if selected_course in self.student_user.course:
            self.alert_label.config(fg="red")
            self.alert_var.set("Course already selected")
            return
        self.student_user.course = self.student_user.course + selected_course + "&" 
        self.alert_label.config(fg="green")
        self.alert_var.set(f"{selected_course} course selected successfully")
        self.update_student_database()

    def update_student_database(self):
        student_database_path = "database/student.txt"
        with open(student_database_path, "r", encoding="utf-8") as rf:
            lines = rf.readlines()
        for i in range(len(lines)):
            if lines[i].startswith(self.student_user.uid):
                lines[i] = f"{self.student_user.uid},{self.student_user.email},{self.student_user.password},{self.student_user.name},{self.student_user.course},{self.student_user.status}\n"
                break
        with open(student_database_path, "w", encoding="utf-8") as wf:
            wf.writelines(lines)

    def load_courses(self):
        self.courses_listbox.delete(0, tk.END)
        available_courses_path = "database/available_courses.txt"
        if os.path.exists(available_courses_path):
            with open(available_courses_path, "r", encoding="utf-8") as rf:
                lines = rf.readlines()
            for line in lines:
                self.courses_listbox.insert(tk.END, line.strip())
            
    def back_to_home_button_clicked(self):
        self.master.hide_available_courses_menu(self)
        self.master.show_student_menu(self.student_menu)
