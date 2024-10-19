import tkinter as tk
from tkinter import ttk
import os
from app.teacher import Teacher

class StaffTeacherMenu(tk.Frame):
    def __init__(self, master, staff_user, staff_menu):
        super().__init__(master)
        self.master = master
        self.staff_user = staff_user
        self.staff_menu = staff_menu

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
        self.tree.column("Course", width=100, anchor=tk.W)
        self.tree.column("Status", width=100, anchor=tk.W)

        # insert data into the table
        self.load_teachers()

        # all teacher heading
        self.heading = tk.Label(self, text="All Teachers", font=("Arial", 18, "bold"))
        self.heading.pack(pady=20)

        # position the Treeview
        self.tree.pack(pady=10)

        # alert variable and label widget
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(self, textvariable=self.alert_var, font=("Arial", 12))
        self.alert_label.pack(pady=10)

        # edit teacher button
        self.edit_teacher_button = tk.Button(self, text="Edit Teacher Details", command=self.edit_teacher_button_clicked)
        self.edit_teacher_button.pack(pady=10)

        # add teacher button
        self.add_teacher_button = tk.Button(self, text="Add Teacher", command=self.add_teacher_button_clicked)
        self.add_teacher_button.pack(pady=10)

        # delete teacher button
        self.delete_teacher_button = tk.Button(self, text="Activate/Deactivate Teacher", command=self.activate_deactivate_teacher_button_clicked)
        self.delete_teacher_button.pack(pady=10)

        # back to home button
        self.back_to_home_button = tk.Button(self, text="Back to Home", command=self.back_to_home_button_clicked)
        self.back_to_home_button.pack(pady=10)

    def edit_teacher_button_clicked(self):
        selected_data = self.tree.focus()
        if not selected_data:
            self.alert_label.config(fg="red")
            self.alert_var.set("Please select a Teacher")
            return
        self.alert_var.set("")
        parent = self.tree.parent(selected_data)
        children = self.tree.get_children(parent)
        self.selected_line = children.index(selected_data)
        teacher_details = self.tree.item(selected_data, "values")
        self.selected_teacher_uid = teacher_details[0]
        self.selected_teacher_email = teacher_details[1]
        self.selected_teacher_password = teacher_details[2]
        self.selected_teacher_name = teacher_details[3]
        self.selected_teacher_course = teacher_details[4]
        teacher_edit_window = tk.Toplevel(self)
        teacher_edit_window.grab_set()
        teacher_edit_window.title(f"Edit Teacher Details")
        teacher_edit_window.geometry("610x390")
        
        # teacher uid label
        teacher_uid_label = tk.Label(teacher_edit_window, text="Teacher UID:", font=("Arial", 12))
        teacher_uid_label.grid(row=0, column=0, padx=10, pady=10)

        # teacher uid entry
        self.teacher_uid_edit_entry = tk.Entry(teacher_edit_window, width=50)
        self.teacher_uid_edit_entry.insert(0, self.selected_teacher_uid)
        self.teacher_uid_edit_entry.grid(row=0, column=1, padx=10, pady=10)

        # teacher email label
        teacher_email_label = tk.Label(teacher_edit_window, text="Teacher Email:", font=("Arial", 12))
        teacher_email_label.grid(row=1, column=0, padx=10, pady=10)

        # teacher email entry
        self.teacher_email_edit_entry = tk.Entry(teacher_edit_window, width=50)
        self.teacher_email_edit_entry.insert(0, self.selected_teacher_email)
        self.teacher_email_edit_entry.grid(row=1, column=1, padx=10, pady=10)

        # teacher password label
        teacher_password_label = tk.Label(teacher_edit_window, text="Teacher Password:", font=("Arial", 12))
        teacher_password_label.grid(row=2, column=0, padx=10, pady=10)

        # teacher password entry
        self.teacher_password_edit_entry = tk.Entry(teacher_edit_window, width=50)
        self.teacher_password_edit_entry.insert(0, self.selected_teacher_password)
        self.teacher_password_edit_entry.grid(row=2, column=1, padx=10, pady=10)

        # teacher name label
        teacher_name_label = tk.Label(teacher_edit_window, text="Teacher Name:", font=("Arial", 12))
        teacher_name_label.grid(row=3, column=0, padx=10, pady=10)

        # teacher name entry
        self.teacher_name_edit_entry = tk.Entry(teacher_edit_window, width=50)
        self.teacher_name_edit_entry.insert(0, self.selected_teacher_name)
        self.teacher_name_edit_entry.grid(row=3, column=1, padx=10, pady=10)

        # teacher course label
        teacher_course_label = tk.Label(teacher_edit_window, text="Teacher Course:", font=("Arial", 12))
        teacher_course_label.grid(row=4, column=0, padx=10, pady=10)

        # teacher course entry
        self.teacher_course_edit_entry = tk.Entry(teacher_edit_window, width=50)
        self.teacher_course_edit_entry.insert(0, self.selected_teacher_course)
        self.teacher_course_edit_entry.grid(row=4, column=1, padx=10, pady=10)

        # alert variable and label widget
        self.alert_var_edit = tk.StringVar()
        self.alert_label_edit = tk.Label(teacher_edit_window, textvariable=self.alert_var_edit, fg="red")        
        self.alert_label_edit.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # save button
        save_button = tk.Button(teacher_edit_window, text="Save", command=self.save_button_clicked)
        save_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # back button
        back_button = tk.Button(teacher_edit_window, text="Back", command=teacher_edit_window.destroy)
        back_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def add_teacher_button_clicked(self):
        self.selected_teacher_email = None
        self.selected_teacher_uid = None
        self.alert_var.set("")
        add_teacher_window = tk.Toplevel(self)
        add_teacher_window.grab_set()
        add_teacher_window.title(f"Add New Teacher")
        add_teacher_window.geometry("610x410")

        # add new teacher heading
        add_new_teacher_heading = tk.Label(add_teacher_window, text="Add New Teacher", font=("Arial", 20))
        add_new_teacher_heading.grid(row=0, columnspan=2, padx=20, pady=10)

        # teacher uid label
        teacher_uid_label = tk.Label(add_teacher_window, text="Teacher UID:", font=("Arial", 12))
        teacher_uid_label.grid(row=1, column=0, padx=10, pady=10)

        # teacher uid entry
        self.teacher_uid_add_entry = tk.Entry(add_teacher_window, width=50)
        self.teacher_uid_add_entry.insert(0, "tea" + str(len(self.tree.get_children()) + 1).zfill(4))
        self.teacher_uid_add_entry.grid(row=1, column=1, padx=10, pady=10)

        # teacher email variable label
        teacher_email_label = tk.Label(add_teacher_window, text="Teacher Email:", font=("Arial", 12))
        teacher_email_label.grid(row=2, column=0, padx=10, pady=10)

        # teacher email entry        
        self.teacher_email_add_entry = tk.Entry(add_teacher_window, width=50)
        self.teacher_email_add_entry.grid(row=2, column=1, padx=10, pady=10)

        # teacher password label
        teacher_password_label = tk.Label(add_teacher_window, text="Teacher Password:", font=("Arial", 12))
        teacher_password_label.grid(row=3, column=0, padx=10, pady=10)

        # teacher password entry
        self.teacher_password_add_entry = tk.Entry(add_teacher_window, width=50)
        self.teacher_password_add_entry.grid(row=3, column=1, padx=10, pady=10)

        # teacher name label
        teacher_name_label = tk.Label(add_teacher_window, text="Teacher Name:", font=("Arial", 12))
        teacher_name_label.grid(row=4, column=0, padx=10, pady=10)

        # teacher name entry
        self.teacher_name_add_entry = tk.Entry(add_teacher_window, width=50)
        self.teacher_name_add_entry.grid(row=4, column=1, padx=10, pady=10)

        # alert variable and label widget
        self.alert_var_add = tk.StringVar()
        self.alert_label_add = tk.Label(add_teacher_window, textvariable=self.alert_var_add, fg="red")        
        self.alert_label_add.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # add button
        add_button = tk.Button(add_teacher_window, text="add", command=lambda:[self.add_button_clicked()])
        add_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # cancel button
        back_button = tk.Button(add_teacher_window, text="Back", command=lambda:[add_teacher_window.destroy()])
        back_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def save_button_clicked(self):
        self.alert_var.set("")
        uid = self.teacher_uid_edit_entry.get()
        name = self.teacher_name_edit_entry.get()
        email = self.teacher_email_edit_entry.get()
        password = self.teacher_password_edit_entry.get()
        course = self.teacher_course_edit_entry.get()

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
        teacher_details = uid + "," + email + "," + password + "," + name + "," + course + ","
        if os.path.exists(self.teacher_path):
            with open(self.teacher_path, "r", encoding="utf-8") as rf:
                data = rf.readlines()
            data[self.selected_line] = teacher_details + "\n"
            with open(self.teacher_path, "w", encoding="utf-8") as wf:
                wf.writelines(data)
            self.load_teachers()
            self.alert_label_edit.config(fg="green")
            self.alert_var_edit.set("Teacher details updated")

    def add_button_clicked(self):
        uid = self.teacher_uid_add_entry.get()
        name = self.teacher_name_add_entry.get()
        email = self.teacher_email_add_entry.get()
        password = self.teacher_password_add_entry.get()

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
        self.add_teacher(uid, name, email, password)
        self.alert_label_add.config(fg="green")
        self.alert_var_add.set(f"Registration successful.")
        self.load_teachers()

    def add_teacher(self, tea_id, name, email, password, course="", status=""):
        if os.path.exists(self.teacher_path):
            with open(self.teacher_path, "a", encoding="utf8") as f:
                new_teacher = f"{tea_id},{email},{password},{name},{course},{status}"
                f.write(new_teacher + "\n")
            
    def activate_deactivate_teacher_button_clicked(self):
        selected_data = self.tree.focus()
        teacher_details = self.tree.item(selected_data, "values")
        if not selected_data:
            self.alert_label.config(fg="red")
            self.alert_var.set("Please select a teacher")
            return
        parent = self.tree.parent(selected_data)
        children = self.tree.get_children(parent)
        self.selected_line = children.index(selected_data)
        if teacher_details[5] == "DEACTIVATED":
            if os.path.exists(self.teacher_path):
                with open(self.teacher_path, "r", encoding="utf-8") as rf:
                    data = rf.readlines()
                data[self.selected_line] = teacher_details[0] + "," + teacher_details[1] + "," + teacher_details[2] + "," + teacher_details[3] + "," + teacher_details[4] + ",\n"
                with open(self.teacher_path, "w", encoding="utf-8") as wf:
                    wf.writelines(data)
                self.load_teachers()
                self.alert_label.config(fg="green")
                self.alert_var.set("Account activated")
                self.load_teachers
                return
        if os.path.exists(self.teacher_path):
            with open(self.teacher_path, "r", encoding="utf-8") as rf:
                data = rf.readlines()
            data[self.selected_line] = teacher_details[0] + "," + teacher_details[1] + "," + teacher_details[2] + "," + teacher_details[3] + "," + teacher_details[4] + ",DEACTIVATED\n"
            with open(self.teacher_path, "w", encoding="utf-8") as wf:
                wf.writelines(data)
            self.load_teachers()
            self.alert_label.config(fg="green")
            self.alert_var.set("Account deactivated")
            self.load_teachers
        
    def load_teachers(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.teacher_path = "database/teacher.txt"
        if os.path.exists(self.teacher_path):
            with open(self.teacher_path, "r", encoding="utf-8") as rf:
                lines = rf.readlines()
            for line in lines:
                self.tree.insert("", tk.END, values=line.strip().split(","))

    def import_teacher(self):
        self.teacher=[]
        if os.path.exists(self.teacher_path):
            with open(self.teacher_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                sta_id, email, password, name, role, status = line.strip().split(",")
                teacher_obj = Teacher(sta_id, email, password, name, role, status)
                self.teacher.append(teacher_obj)
            return self.teacher

    def check_duplicate_uid(self, uid):
        self.import_teacher()
        for teacher in self.teacher:
            if teacher.uid == self.selected_teacher_uid:
                continue
            if teacher.uid == uid:
                return True
        return False

    def check_duplicate_email(self, email):
        self.import_teacher()
        for teacher in self.teacher:
            if teacher.email == self.selected_teacher_email:
                continue
            if teacher.email == email:
                return True
        return False

    def back_to_home_button_clicked(self):
        self.master.hide_staff_staff_menu(self)
        self.master.show_staff_menu(self.staff_menu)