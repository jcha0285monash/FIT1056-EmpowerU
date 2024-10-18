import tkinter as tk
from tkinter import simpledialog, messagebox
import os
from interface.teacher_menus.editcourse import EditCourseContentPage

class TeacherCoursesMenu(tk.Frame):
    def __init__(self, master, teacher_user, teacher_menu):
        super().__init__(master)
        self.master = master
        self.teacher_user = teacher_user
        self.teacher_menu = teacher_menu

        # all courses heading
        self.heading = tk.Label(self, text="All Courses", font=("Arial", 18, "bold"))
        self.heading.pack(pady=20)

        # all courses listbox
        self.courses_listbox = tk.Listbox(self, width=50, height=10)
        self.courses_listbox.pack(pady=20)

        # alert variable and label widget
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(self, textvariable=self.alert_var, font=("Arial", 12))
        self.alert_label.pack(pady=10)

        # "Edit Course Content" button to navigate to content editor
        self.edit_course_content_button = tk.Button(self, text="Edit Course Content", command=self.edit_course_content)
        self.edit_course_content_button.pack(pady=10)

        # back to home button
        self.back_to_home_button = tk.Button(self, text="Back to Home", command=self.back_to_home_button_clicked)
        self.back_to_home_button.pack(pady=10)

        # Load the courses
        self.load_courses()

    def load_courses(self):
        """Loads the courses from available_courses.txt into the listbox."""
        self.courses_listbox.delete(0, tk.END)
        available_courses_path = "database/available_courses.txt"
        if os.path.exists(available_courses_path):
            with open(available_courses_path, "r", encoding="utf-8") as rf:
                lines = rf.readlines()
            for line in lines:
                self.courses_listbox.insert(tk.END, line.strip())

    def edit_course_content(self):
        """Opens a new window to edit the course and task content."""
        selected_course_index = self.courses_listbox.curselection()
        if selected_course_index:
            selected_course = self.courses_listbox.get(selected_course_index)
            # Hide the current menu and open the edit page
            self.pack_forget()
            edit_page = EditCourseContentPage(self.master, selected_course, self)
            edit_page.pack(fill="both", expand=True)


    def back_to_home_button_clicked(self):
        self.pack_forget()
        self.teacher_menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
