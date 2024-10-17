import tkinter as tk
from tkinter import simpledialog, messagebox
import os
from interface.staff_menus.editcourse import EditCourseContentPage

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

        # alert variable and label widget
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(self, textvariable=self.alert_var, font=("Arial", 12))
        self.alert_label.pack(pady=10)

        # Buttons for course and task management
        self.edit_course_button = tk.Button(self, text="Edit Course", command=self.edit_course_button_clicked)
        self.edit_course_button.pack(pady=5)

        self.add_course_button = tk.Button(self, text="Add New Course", command=self.add_course)
        self.add_course_button.pack(pady=5)

        self.delete_course_button = tk.Button(self, text="Delete Course", command=self.delete_course)
        self.delete_course_button.pack(pady=5)

        # "Edit Course Content" button to navigate to content editor
        self.edit_course_content_button = tk.Button(self, text="Edit Course Content", command=self.edit_course_content)
        self.edit_course_content_button.pack(pady=10)

        # back to home button
        self.back_to_home_button = tk.Button(self, text="Back to Home", command=self.back_to_home_button_clicked)
        self.back_to_home_button.pack(pady=10)

        # Load the initial courses
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

    def edit_course_button_clicked(self):
        """Allows the staff to edit the selected course."""
        selected_course_index = self.courses_listbox.curselection()
        if selected_course_index:
            selected_course = self.courses_listbox.get(selected_course_index)
            new_name = simpledialog.askstring("Edit Course", "Enter the new course name:", initialvalue=selected_course)
            if new_name:
                self.update_course_in_file(selected_course, new_name)

    def update_course_in_file(self, old_name, new_name):
        """Updates the course name in the file."""
        available_courses_path = "database/available_courses.txt"
        with open(available_courses_path, "r", encoding="utf-8") as rf:
            courses = rf.readlines()
        courses = [new_name + "\n" if course.strip() == old_name else course for course in courses]

        with open(available_courses_path, "w", encoding="utf-8") as wf:
            wf.writelines(courses)

        # Rename the associated task file if it exists
        old_tasks_path = f"database/{old_name}_tasks.txt"
        new_tasks_path = f"database/{new_name}_tasks.txt"
        if os.path.exists(old_tasks_path):
            os.rename(old_tasks_path, new_tasks_path)

        self.load_courses()

    def add_course(self):
        """Adds a new course to the available_courses.txt file."""
        new_course = simpledialog.askstring("New Course", "Enter the name of the new course:")
        if new_course:
            available_courses_path = "database/available_courses.txt"
            with open(available_courses_path, "a", encoding="utf-8") as wf:
                wf.write(new_course + "\n")
            self.load_courses()

    def delete_course(self):
        """Deletes the selected course from the available_courses.txt file."""
        selected_course_index = self.courses_listbox.curselection()
        if selected_course_index:
            selected_course = self.courses_listbox.get(selected_course_index)
            confirmation = messagebox.askyesno("Delete Course", f"Are you sure you want to delete {selected_course}?")
            if confirmation:
                available_courses_path = "database/available_courses.txt"
                with open(available_courses_path, "r", encoding="utf-8") as rf:
                    courses = rf.readlines()
                courses = [course for course in courses if course.strip() != selected_course]

                with open(available_courses_path, "w", encoding="utf-8") as wf:
                    wf.writelines(courses)

                # Delete the associated task file if it exists
                tasks_path = f"database/{selected_course}_tasks.txt"
                if os.path.exists(tasks_path):
                    os.remove(tasks_path)

                self.load_courses()
                self.tasks_listbox.delete(0, tk.END)

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
        self.master.hide_staff_courses_menu(self)
        self.master.show_staff_menu(self.staff_menu)
