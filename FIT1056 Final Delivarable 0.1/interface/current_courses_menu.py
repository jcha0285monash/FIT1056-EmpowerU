import tkinter as tk

class CurrentCoursesMenu(tk.Frame):
    def __init__(self, master, student_user, student_menu):
        super().__init__(master)
        self.master = master
        self.student_user = student_user
        self.student_menu = student_menu

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

        # back to home button
        self.back_to_home_button = tk.Button(self, text="Back to Home", command=self.back_to_home_button_clicked)
        self.back_to_home_button.pack(pady=10)

    def load_courses(self):
        self.courses_list.delete(0, tk.END)
        current_courses = self.student_user.course.split("&")
        for courses in current_courses:
            if courses != "":
                self.courses_list.insert(tk.END, courses)

    def back_to_home_button_clicked(self):
        self.master.hide_available_courses_menu(self)
        self.master.show_student_menu(self.student_menu)
