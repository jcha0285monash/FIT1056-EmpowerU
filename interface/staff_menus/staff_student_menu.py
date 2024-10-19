import tkinter as tk
from tkinter import ttk
import os
from app.student import Student

class StaffStudentMenu(tk.Frame):
    def __init__(self, master, staff_user, staff_menu):
        super().__init__(master)
        self.master = master
        self.staff_user = staff_user
        self.staff_menu = staff_menu

        style = ttk.Style()
        style.configure("Treeview", rowheight=47)  # Change row height to fit 3 courses

        # create tree view
        self.tree = ttk.Treeview(self, columns=("UID", "Email", "Password", "Name", "Course", "Status"), show="headings")
        self.tree.heading("UID", text="UID")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Password", text="Password")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Course", text="Course")
        self.tree.heading("Status", text="Status")

        # define column width and alignment
        self.tree.column("UID", width=100, anchor=tk.CENTER)
        self.tree.column("Email", width=150, anchor=tk.W)
        self.tree.column("Password", width=100, anchor=tk.W)
        self.tree.column("Name", width=150, anchor=tk.W)
        self.tree.column("Course", width=200, anchor=tk.W)
        self.tree.column("Status", width=85, anchor=tk.CENTER)

        # insert data into the table
        self.load_students()

        # all student heading
        self.heading = tk.Label(self, text="All Students", font=("Arial", 18, "bold"))
        self.heading.grid(row=0, columnspan=4, padx=20, pady=10)

        # position the Treeview
        self.tree.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        # alert variable and label widget
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(self, textvariable=self.alert_var, font=("Arial", 12))
        self.alert_label.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        # edit student button
        self.edit_student_button = tk.Button(self, text="Edit Student Details", command=self.edit_student_button_clicked)
        self.edit_student_button.grid(row=3, column=0, padx=10, pady=10)

        # add student button
        self.add_student_button = tk.Button(self, text="Add Student", command=self.add_student_button_clicked)
        self.add_student_button.grid(row=3, column=1, padx=10, pady=10)

        # delete student button
        self.delete_student_button = tk.Button(self, text="Activate/Deactivate Student", command=self.activate_deactivate_student_button_clicked)
        self.delete_student_button.grid(row=3, column=2, padx=10, pady=10)

        # back to home button
        self.back_to_home_button = tk.Button(self, text="Back to Home", command=self.back_to_home_button_clicked)
        self.back_to_home_button.grid(row=3, column=3, padx=10, pady=10)

    def edit_student_button_clicked(self):
        selected_data = self.tree.focus()
        if not selected_data:
            self.alert_label.config(fg="red")
            self.alert_var.set("Please select a student")
            return
        self.alert_var.set("")
        parent = self.tree.parent(selected_data)
        children = self.tree.get_children(parent)
        self.selected_line = children.index(selected_data)
        student_details = self.tree.item(selected_data, "values")
        self.selected_student_uid = student_details[0]
        self.selected_student_email = student_details[1]
        self.selected_student_password = student_details[2]
        self.selected_student_name = student_details[3]
        self.selected_student_course = student_details[4]
        self.selected_student_status = student_details[5]
        student_edit_window = tk.Toplevel(self)
        student_edit_window.grab_set()
        student_edit_window.title(f"Edit Student Details")
        student_edit_window.geometry("610x420")
        
        # student uid label
        student_uid_label = tk.Label(student_edit_window, text="Student UID:", font=("Arial", 12))
        student_uid_label.grid(row=0, column=0, padx=10, pady=10)

        # student uid entry
        self.student_uid_edit_entry = tk.Entry(student_edit_window, width=50)
        self.student_uid_edit_entry.insert(0, self.selected_student_uid)
        self.student_uid_edit_entry.grid(row=0, column=1, padx=10, pady=10)

        # student email label
        student_email_label = tk.Label(student_edit_window, text="Student Email:", font=("Arial", 12))
        student_email_label.grid(row=1, column=0, padx=10, pady=10)

        # student email entry
        self.student_email_edit_entry = tk.Entry(student_edit_window, width=50)
        self.student_email_edit_entry.insert(0, self.selected_student_email)
        self.student_email_edit_entry.grid(row=1, column=1, padx=10, pady=10)

        # student password label
        student_password_label = tk.Label(student_edit_window, text="Student Password:", font=("Arial", 12))
        student_password_label.grid(row=2, column=0, padx=10, pady=10)

        # student password entry
        self.student_password_edit_entry = tk.Entry(student_edit_window, width=50)
        self.student_password_edit_entry.insert(0, self.selected_student_password)
        self.student_password_edit_entry.grid(row=2, column=1, padx=10, pady=10)

        # student name label
        student_name_label = tk.Label(student_edit_window, text="Student Name:", font=("Arial", 12))
        student_name_label.grid(row=3, column=0, padx=10, pady=10)

        # student name entry
        self.student_name_edit_entry = tk.Entry(student_edit_window, width=50)
        self.student_name_edit_entry.insert(0, self.selected_student_name)
        self.student_name_edit_entry.grid(row=3, column=1, padx=10, pady=10)

        # student course label
        student_course_label = tk.Label(student_edit_window, text="Student Course:", font=("Arial", 12))
        student_course_label.grid(row=4, column=0, padx=10, pady=10)

        # student course text widget entry
        self.student_course_edit_entry = tk.Text(student_edit_window, width=50, height=5)
        self.student_course_edit_entry.insert(tk.END, self.selected_student_course)
        self.student_course_edit_entry.grid(row=4, column=1, padx=10, pady=10)

        # alert variable and label widget
        self.alert_var_edit = tk.StringVar()
        self.alert_label_edit = tk.Label(student_edit_window, textvariable=self.alert_var_edit, fg="red")        
        self.alert_label_edit.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # save button
        save_button = tk.Button(student_edit_window, text="Save", command=self.save_button_clicked)
        save_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # back button
        back_button = tk.Button(student_edit_window, text="Back", command=student_edit_window.destroy)
        back_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def add_student_button_clicked(self):
        self.selected_student_email = None
        self.selected_student_uid = None
        self.alert_var.set("")
        add_student_window = tk.Toplevel(self)
        add_student_window.grab_set()
        add_student_window.title(f"Add New Student")
        add_student_window.geometry("610x410")

        # add new student heading
        add_new_student_heading = tk.Label(add_student_window, text="Add New Student", font=("Arial", 20))
        add_new_student_heading.grid(row=0, columnspan=2, padx=20, pady=10)

        # student uid label
        student_uid_label = tk.Label(add_student_window, text="Student UID:", font=("Arial", 12))
        student_uid_label.grid(row=1, column=0, padx=10, pady=10)

        # student uid entry
        self.student_uid_add_entry = tk.Entry(add_student_window, width=50)
        self.student_uid_add_entry.insert(0, "stu" + str(len(self.tree.get_children()) + 1).zfill(4))
        self.student_uid_add_entry.grid(row=1, column=1, padx=10, pady=10)

        # student email variable label
        student_email_label = tk.Label(add_student_window, text="Student Email:", font=("Arial", 12))
        student_email_label.grid(row=2, column=0, padx=10, pady=10)

        # student email entry        
        self.student_email_add_entry = tk.Entry(add_student_window, width=50)
        self.student_email_add_entry.grid(row=2, column=1, padx=10, pady=10)

        # student password label
        student_password_label = tk.Label(add_student_window, text="Student Password:", font=("Arial", 12))
        student_password_label.grid(row=3, column=0, padx=10, pady=10)

        # student password entry
        self.student_password_add_entry = tk.Entry(add_student_window, width=50)
        self.student_password_add_entry.grid(row=3, column=1, padx=10, pady=10)

        # student name label
        student_name_label = tk.Label(add_student_window, text="Student Name:", font=("Arial", 12))
        student_name_label.grid(row=4, column=0, padx=10, pady=10)

        # student name entry
        self.student_name_add_entry = tk.Entry(add_student_window, width=50)
        self.student_name_add_entry.grid(row=4, column=1, padx=10, pady=10)

        # alert variable and label widget
        self.alert_var_add = tk.StringVar()
        self.alert_label_add = tk.Label(add_student_window, textvariable=self.alert_var_add, fg="red")        
        self.alert_label_add.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # add button
        add_button = tk.Button(add_student_window, text="add", command=lambda:[self.add_button_clicked()])
        add_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # cancel button
        back_button = tk.Button(add_student_window, text="Back", command=lambda:[add_student_window.destroy()])
        back_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def save_button_clicked(self):
        self.alert_var.set("")
        uid = self.student_uid_edit_entry.get()
        name = self.student_name_edit_entry.get()
        email = self.student_email_edit_entry.get()
        password = self.student_password_edit_entry.get()
        new_course = self.student_course_edit_entry.get("1.0", tk.END).strip().split("\n")

        # join courses in text widget with &
        if len(new_course) == 1:
            new_course[0] += "&"
        course = "&".join(new_course)

        if uid == "" or name == "" or email == "" or password == "":
            self.alert_var_edit.set("Please fill in all fields")
            return
        elif self.check_duplicate_email(email):
            self.alert_label_edit.config(fg="red")
            self.alert_var_edit.set("Email already exists")
            return
        elif "@" not in email or "." not in email:
            self.alert_label_edit.config(fg="red")
            self.alert_var_edit.set("Invalid email")
            return
        elif self.check_duplicate_uid(uid):
            self.alert_label_edit.config(fg="red")
            self.alert_var_edit.set("UID already exists")
            return
        student_details = uid + "," + email + "," + password + "," + name + "," + course + "," + self.selected_student_status
        if os.path.exists(self.student_path):
            with open(self.student_path, "r", encoding="utf-8") as rf:
                data = rf.readlines()
            data[self.selected_line] = student_details + "\n"
            with open(self.student_path, "w", encoding="utf-8") as wf:
                wf.writelines(data)
            self.load_students()
            self.alert_label_edit.config(fg="green")
            self.alert_var_edit.set("Student details updated")

    def add_button_clicked(self):
        uid = self.student_uid_add_entry.get()
        name = self.student_name_add_entry.get()
        email = self.student_email_add_entry.get()
        password = self.student_password_add_entry.get()

        if self.check_duplicate_uid(uid):
            self.alert_label_add.config(fg="red")
            self.alert_var_add.set("UID already exists")
            return
        elif self.check_duplicate_email(email):
            self.alert_label_add.config(fg="red")
            self.alert_var_add.set("Email already exists")
            return
        elif uid == "" or name == "" or email == "" or password == "":
            self.alert_label_add.config(fg="red")
            self.alert_var_add.set("Please fill in all fields")
            return
        elif "@" not in email or "." not in email:
            self.alert_label_add.config(fg="red")
            self.alert_var_add.set("Invalid email")
            return
        self.add_student(uid, name, email, password)
        self.alert_label_add.config(fg="green")
        self.alert_var_add.set(f"Registration successful.")
        self.load_students()

    def add_student(self, stu_id, name, email, password, course="", status=""):
        if os.path.exists(self.student_path):
            with open(self.student_path, "a", encoding="utf8") as f:
                new_student = f"{stu_id},{email},{password},{name},{course},{status}"
                f.write(new_student + "\n")
            
    def activate_deactivate_student_button_clicked(self):
        selected_data = self.tree.focus()
        student_details = self.tree.item(selected_data, "values")
        if not selected_data:
            self.alert_label.config(fg="red")
            self.alert_var.set("Please select a student")
            return
        parent = self.tree.parent(selected_data)
        children = self.tree.get_children(parent)
        self.selected_line = children.index(selected_data)
        student_courses = student_details[4].replace("\n", "&")
        if student_details[5] == "DEACTIVATED":
            if os.path.exists(self.student_path):
                with open(self.student_path, "r", encoding="utf-8") as rf:
                    data = rf.readlines()
                data[self.selected_line] = student_details[0] + "," + student_details[1] + "," + student_details[2] + "," + student_details[3] + "," + student_courses + ",ACTIVE\n"
                with open(self.student_path, "w", encoding="utf-8") as wf:
                    wf.writelines(data)
                self.load_students()
                self.alert_label.config(fg="green")
                self.alert_var.set("Account activated")
                self.load_students
                return
        if os.path.exists(self.student_path):
            with open(self.student_path, "r", encoding="utf-8") as rf:
                data = rf.readlines()
            data[self.selected_line] = student_details[0] + "," + student_details[1] + "," + student_details[2] + "," + student_details[3] + "," + student_courses + ",DEACTIVATED\n"
            with open(self.student_path, "w", encoding="utf-8") as wf:
                wf.writelines(data)
            self.load_students()
            self.alert_label.config(fg="green")
            self.alert_var.set("Account deactivated")
            self.load_students
        
    def load_students(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.student_path = "./database/student.txt"
        if os.path.exists(self.student_path):
            with open(self.student_path, "r", encoding="utf-8") as rf:
                lines = rf.readlines()
            for line in lines:
                values = line.strip().split(",")
                values[4] = values[4].replace("&", "\n")
                self.tree.insert("", tk.END, values=values)

    def import_student(self):
        self.student=[]
        if os.path.exists(self.student_path):
            with open(self.student_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                sta_id, email, password, name, role, status = line.strip().split(",")
                student_obj = Student(sta_id, email, password, name, role, status)
                self.student.append(student_obj)
            return self.student

    def check_duplicate_uid(self, uid):
        self.import_student()
        for student in self.student:
            if student.uid == self.selected_student_uid:
                continue
            if student.uid == uid:
                return True
        return False

    def check_duplicate_email(self, email):
        self.import_student()
        for student in self.student:
            if student.email == self.selected_student_email:
                continue
            if student.email == email:
                return True
        return False

    def back_to_home_button_clicked(self):
        self.master.hide_staff_staff_menu(self)
        self.master.show_staff_menu(self.staff_menu)