import tkinter as tk
from tkinter import ttk
import os

class StaffStudentMenu(tk.Frame):
    def __init__(self, master, staff_user, staff_menu):
        super().__init__(master)
        self.master = master
        self.staff_user = staff_user
        self.staff_menu = staff_menu

        style = ttk.Style()
        style.configure("Treeview", rowheight=47)  # Set the row height to accommodate up to 3 courses

        # create tree view
        self.tree = ttk.Treeview(self, columns=("UID", "Email", "Password", "Name", "Course"), show="headings")
        self.tree.heading("UID", text="UID")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Password", text="Password")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Course", text="Course")

        # define column width and alignment
        self.tree.column("UID", width=80, anchor=tk.CENTER)
        self.tree.column("Email", width=150, anchor=tk.W)
        self.tree.column("Password", width=100, anchor=tk.W)
        self.tree.column("Name", width=150, anchor=tk.W)
        self.tree.column("Course", width=150, anchor=tk.W)

        # insert data into the table
        self.load_students()

        # all student heading
        self.heading = tk.Label(self, text="All Students", font=("Arial", 18, "bold"))
        self.heading.pack(pady=20)

        # position the Treeview
        self.tree.pack(pady=1)

        # alert variable and label widget
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(self, textvariable=self.alert_var, font=("Arial", 12))
        self.alert_label.pack(pady=10)

        # edit student button
        self.edit_student_button = tk.Button(self, text="Edit Student Details", command=self.edit_student_button_clicked)
        self.edit_student_button.pack(pady=10)

        # add student button
        self.add_student_button = tk.Button(self, text="Add Student", command=self.add_student_button_clicked)
        self.add_student_button.pack(pady=10)

        # delete student button
        self.delete_student_button = tk.Button(self, text="Delete Student", command=self.delete_student_button_clicked)
        self.delete_student_button.pack(pady=10)

        # back to home button
        self.back_to_home_button = tk.Button(self, text="Back to Home", command=self.back_to_home_button_clicked)
        self.back_to_home_button.pack(pady=10)

    def load_students(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.student_path = "./database/student.txt"
        if os.path.exists(self.student_path):
            with open(self.student_path, "r", encoding="utf-8") as rf:
                lines = rf.readlines()
            for line in lines:
                values = line.strip().split(",")
                values[4] = values[4].replace("&", "\n")  # Replace & with a new line
                self.tree.insert("", tk.END, values=values)

    def edit_student_button_clicked(self):
        selected_data = self.tree.focus()
        if not selected_data:
            self.alert_label.config(fg="red")
            self.alert_var.set("Please select a student")
            return
        self.alert_var.set("")
        parent = self.tree.parent(selected_data)
        children = self.tree.get_children(parent)
        selected_line = children.index(selected_data)
        student_details = self.tree.item(selected_data, "values")
        student_user_uid = student_details[0]
        student_user_email = student_details[1]
        student_user_password = student_details[2]
        student_user_name = student_details[3]
        student_user_course = student_details[4]
        self.student_edit_window = tk.Toplevel(self)
        self.student_edit_window.title(f"Edit Student Details")
        self.student_edit_window.geometry("610x500")
        
        # student uid label
        student_uid_label = tk.Label(self.student_edit_window, text="Student UID:", font=("Arial", 12))
        student_uid_label.grid(row=0, column=0, padx=10, pady=10)

        # student uid entry
        self.student_uid_entry = tk.Entry(self.student_edit_window, width=50)
        self.student_uid_entry.insert(0, student_user_uid)
        self.student_uid_entry.grid(row=0, column=1, padx=10, pady=10)

        # student email label
        student_email_label = tk.Label(self.student_edit_window, text="Student Email:", font=("Arial", 12))
        student_email_label.grid(row=1, column=0, padx=10, pady=10)

        # student email entry
        self.student_email_entry = tk.Entry(self.student_edit_window, width=50)
        self.student_email_entry.insert(0, student_user_email)
        self.student_email_entry.grid(row=1, column=1, padx=10, pady=10)

        # student password label
        student_password_label = tk.Label(self.student_edit_window, text="Student Password:", font=("Arial", 12))
        student_password_label.grid(row=2, column=0, padx=10, pady=10)

        # student password entry
        self.student_password_entry = tk.Entry(self.student_edit_window, width=50)
        self.student_password_entry.insert(0, student_user_password)
        self.student_password_entry.grid(row=2, column=1, padx=10, pady=10)

        # student name label
        student_name_label = tk.Label(self.student_edit_window, text="Student Name:", font=("Arial", 12))
        student_name_label.grid(row=3, column=0, padx=10, pady=10)

        # student name entry
        self.student_name_entry = tk.Entry(self.student_edit_window, width=50)
        self.student_name_entry.insert(0, student_user_name)
        self.student_name_entry.grid(row=3, column=1, padx=10, pady=10)

        # student course label
        student_course_label = tk.Label(self.student_edit_window, text="Student Course:", font=("Arial", 12))
        student_course_label.grid(row=4, column=0, padx=10, pady=10)

        # student course text widget
        self.student_course_text = tk.Text(self.student_edit_window, width=50, height=10)
        self.student_course_text.grid(row=4, column=1, padx=10, pady=10)

        # Insert each course into the text widget
        courses = student_user_course.split("&")
        for course in courses:
            self.student_course_text.insert(tk.END, course + "\n")

        # save button
        save_button = tk.Button(self.student_edit_window, text="Save", command=lambda:[self.save_button_clicked(selected_line)])
        save_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # back button
        back_button = tk.Button(self.student_edit_window, text="Back", command=self.student_edit_window.destroy)
        back_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def add_student_button_clicked(self):
        self.student_register_window = tk.Toplevel(self)
        self.student_register_window.title(f"Add New Student")
        self.student_register_window.geometry("610x410")

        # add new student heading
        self.add_new_student_heading = tk.Label(self.student_register_window, text="Add New Student", font=("Arial", 20))
        self.add_new_student_heading.grid(row=0, columnspan=2, padx=20, pady=10)

        # student uid label
        student_uid_label = tk.Label(self.student_register_window, text="Student UID:", font=("Arial", 12))
        student_uid_label.grid(row=1, column=0, padx=10, pady=10)

        # student uid entry
        self.student_uid_entry = tk.Entry(self.student_register_window, width=50)
        self.student_uid_entry.insert(0, "stu" + str(len(self.tree.get_children()) + 1).zfill(4))
        self.student_uid_entry.grid(row=1, column=1, padx=10, pady=10)

        # student email variable label
        student_email_label = tk.Label(self.student_register_window, text="Student Email:", font=("Arial", 12))
        student_email_label.grid(row=2, column=0, padx=10, pady=10)

        # student email entry        
        self.student_email_entry = tk.Entry(self.student_register_window, width=50)
        self.student_email_entry.grid(row=2, column=1, padx=10, pady=10)

        # student password label
        student_password_label = tk.Label(self.student_register_window, text="Student Password:", font=("Arial", 12))
        student_password_label.grid(row=3, column=0, padx=10, pady=10)

        # student password entry
        self.student_password_entry = tk.Entry(self.student_register_window, width=50)
        self.student_password_entry.grid(row=3, column=1, padx=10, pady=10)

        # student name label
        student_name_label = tk.Label(self.student_register_window, text="Student Name:", font=("Arial", 12))
        student_name_label.grid(row=4, column=0, padx=10, pady=10)

        # student name entry
        self.student_name_entry = tk.Entry(self.student_register_window, width=50)
        self.student_name_entry.grid(row=4, column=1, padx=10, pady=10)

        # alert variable and label widget
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(self.student_register_window, textvariable=self.alert_var, fg="red")        
        self.alert_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # register button
        register_button = tk.Button(self.student_register_window, text="Register", command=lambda:[self.register_button_clicked()])
        register_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # cancel button
        back_button = tk.Button(self.student_register_window, text="Back", command=lambda:[self.student_register_window.destroy()])
        back_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def save_button_clicked(self, selected_line):
        courses = self.student_course_text.get("1.0", tk.END).strip().split("\n")
        # Handle the case where there is only one course
        if len(courses) == 1:
            courses[0] += "&"
        
        # Join the courses with &
        joined_courses = "&".join(courses)
        
        student_details = (
            self.student_uid_entry.get() + "," +
            self.student_email_entry.get() + "," +
            self.student_password_entry.get() + "," +
            self.student_name_entry.get() + "," +
            joined_courses + "," +
            "ACTIVE"
        )

        if os.path.exists(self.student_path):
            with open(self.student_path, "r", encoding="utf-8") as rf:
                data = rf.readlines()
            data[selected_line] = student_details + "\n"
            with open(self.student_path, "w", encoding="utf-8") as wf:
                wf.writelines(data)
            self.load_students()


    def register_button_clicked(self):
        pass
        uid = self.student_uid_entry.get()
        name = self.student_name_entry.get()
        email = self.student_email_entry.get()
        password = self.student_password_entry.get()

        if uid in self.tree.get_children():
            self.alert_label.config(fg="red")
            self.alert_var.set("UID already exists")
        elif uid == "" or name == "" or email == "" or password == "":
            self.alert_label.config(fg="red")
            self.alert_var.set("Please fill in all fields")
        elif email in self.tree.get_children():
            self.alert_label.config(fg="red")
            self.alert_var.set("Email already exists")
        elif "@" not in email or "." not in email:
            self.alert_label.config(fg="red")
            self.alert_var.set("Invalid email")
        else:
            self.register_student(uid, name, email, password)
            self.alert_label.config(fg="green")
            self.alert_var.set(f"Registration successful.")
            self.load_students()

    def register_student(self, stu_id, name, email, password, course=""):
        student_path = "./database/student.txt"
        if os.path.exists(student_path):
            with open(student_path, "a", encoding="utf8") as f:
                new_student = f"{stu_id},{email},{password},{name},{course}"
                f.write(new_student + "\n")
            
    def delete_student_button_clicked(self):
        selected_data = self.tree.focus()
        print(selected_data)
        if not selected_data:
            self.alert_label.config(fg="red")
            self.alert_var.set("Please select a student")
            return
        parent = self.tree.parent(selected_data)
        children = self.tree.get_children(parent)
        selected_line = children.index(selected_data)
        self.alert_var.set("")
        if os.path.exists(self.student_path):
            with open(self.student_path, "r", encoding="utf-8") as rf:
                data = rf.readlines()
            if 0 <= selected_line <= len(data):
                del data[selected_line]
            with open(self.student_path, "w", encoding="utf-8") as wf:
                wf.writelines(data)
            self.load_students()

    def back_to_home_button_clicked(self):
        self.master.hide_staff_staff_menu(self)
        self.master.show_staff_menu(self.staff_menu)
