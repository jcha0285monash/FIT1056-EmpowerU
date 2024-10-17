import tkinter as tk
from tkinter import ttk
import os

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

    def load_teachers(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.teacher_path = "./database/teacher.txt"
        if os.path.exists(self.teacher_path):
            with open(self.teacher_path, "r", encoding="utf-8") as rf:
                lines = rf.readlines()
            for line in lines:
                self.tree.insert("", tk.END, values=line.strip().split(","))

    def edit_teacher_button_clicked(self):
        selected_data = self.tree.focus()
        if not selected_data:
            self.alert_label.config(fg="red")
            self.alert_var.set("Please select a teacher")
            return
        self.alert_var.set("")
        parent = self.tree.parent(selected_data)
        children = self.tree.get_children(parent)
        self.selected_line = children.index(selected_data)
        teacher_details = self.tree.item(selected_data, "values")
        teacher_user_uid = teacher_details[0]
        teacher_user_email = teacher_details[1]
        teacher_user_password = teacher_details[2]
        teacher_user_name = teacher_details[3]
        teacher_user_course = teacher_details[4]
        self.teacher_edit_window = tk.Toplevel(self)
        self.teacher_edit_window.title(f"Edit Teacher Details")
        self.teacher_edit_window.geometry("610x390")
        
        # teacher uid label
        teacher_uid_label = tk.Label(self.teacher_edit_window, text="Teacher UID:", font=("Arial", 12))
        teacher_uid_label.grid(row=0, column=0, padx=10, pady=10)

        # teacher uid entry
        self.teacher_uid_entry = tk.Entry(self.teacher_edit_window, width=50)
        self.teacher_uid_entry.insert(0, teacher_user_uid)
        self.teacher_uid_entry.grid(row=0, column=1, padx=10, pady=10)

        # teacher email label
        teacher_email_label = tk.Label(self.teacher_edit_window, text="Teacher Email:", font=("Arial", 12))
        teacher_email_label.grid(row=1, column=0, padx=10, pady=10)

        # teacher email entry
        self.teacher_email_entry = tk.Entry(self.teacher_edit_window, width=50)
        self.teacher_email_entry.insert(0, teacher_user_email)
        self.teacher_email_entry.grid(row=1, column=1, padx=10, pady=10)

        # teacher password label
        teacher_password_label = tk.Label(self.teacher_edit_window, text="Teacher Password:", font=("Arial", 12))
        teacher_password_label.grid(row=2, column=0, padx=10, pady=10)

        # teacher password entry
        self.teacher_password_entry = tk.Entry(self.teacher_edit_window, width=50)
        self.teacher_password_entry.insert(0, teacher_user_password)
        self.teacher_password_entry.grid(row=2, column=1, padx=10, pady=10)

        # teacher name label
        teacher_name_label = tk.Label(self.teacher_edit_window, text="Teacher Name:", font=("Arial", 12))
        teacher_name_label.grid(row=3, column=0, padx=10, pady=10)

        # teacher name entry
        self.teacher_name_entry = tk.Entry(self.teacher_edit_window, width=50)
        self.teacher_name_entry.insert(0, teacher_user_name)
        self.teacher_name_entry.grid(row=3, column=1, padx=10, pady=10)

        # teacher course label
        teacher_course_label = tk.Label(self.teacher_edit_window, text="Teacher Course:", font=("Arial", 12))
        teacher_course_label.grid(row=4, column=0, padx=10, pady=10)

        # teacher course entry
        self.teacher_course_entry = tk.Entry(self.teacher_edit_window, width=50)
        self.teacher_course_entry.insert(0, teacher_user_course)
        self.teacher_course_entry.grid(row=4, column=1, padx=10, pady=10)

        # alert variable and label widget
        self.alert_var_edit = tk.StringVar()
        self.alert_label_edit = tk.Label(self.teacher_edit_window, textvariable=self.alert_var_edit, fg="red")        
        self.alert_label_edit.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # save button
        save_button = tk.Button(self.teacher_edit_window, text="Save", command=self.save_button_clicked)
        save_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # back button
        back_button = tk.Button(self.teacher_edit_window, text="Back", command=self.teacher_edit_window.destroy)
        back_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def add_teacher_button_clicked(self):
        self.teacher_register_window = tk.Toplevel(self)
        self.teacher_register_window.title(f"Add New Teacher")
        self.teacher_register_window.geometry("610x410")

        # add new teacher heading
        self.add_new_teacher_heading = tk.Label(self.teacher_register_window, text="Add New Teacher", font=("Arial", 20))
        self.add_new_teacher_heading.grid(row=0, columnspan=2, padx=20, pady=10)

        # teacher uid label
        teacher_uid_label = tk.Label(self.teacher_register_window, text="Teacher UID:", font=("Arial", 12))
        teacher_uid_label.grid(row=1, column=0, padx=10, pady=10)

        # teacher uid entry
        self.teacher_uid_entry = tk.Entry(self.teacher_register_window, width=50)
        self.teacher_uid_entry.insert(0, "tea" + str(len(self.tree.get_children()) + 1).zfill(4))
        self.teacher_uid_entry.grid(row=1, column=1, padx=10, pady=10)

        # teacher email variable label
        teacher_email_label = tk.Label(self.teacher_register_window, text="Teacher Email:", font=("Arial", 12))
        teacher_email_label.grid(row=2, column=0, padx=10, pady=10)

        # teacher email entry        
        self.teacher_email_entry = tk.Entry(self.teacher_register_window, width=50)
        self.teacher_email_entry.grid(row=2, column=1, padx=10, pady=10)

        # teacher password label
        teacher_password_label = tk.Label(self.teacher_register_window, text="Teacher Password:", font=("Arial", 12))
        teacher_password_label.grid(row=3, column=0, padx=10, pady=10)

        # teacher password entry
        self.teacher_password_entry = tk.Entry(self.teacher_register_window, width=50)
        self.teacher_password_entry.grid(row=3, column=1, padx=10, pady=10)

        # teacher name label
        teacher_name_label = tk.Label(self.teacher_register_window, text="Teacher Name:", font=("Arial", 12))
        teacher_name_label.grid(row=4, column=0, padx=10, pady=10)

        # teacher name entry
        self.teacher_name_entry = tk.Entry(self.teacher_register_window, width=50)
        self.teacher_name_entry.grid(row=4, column=1, padx=10, pady=10)

        # alert variable and label widget
        self.alert_var_add = tk.StringVar()
        self.alert_label_add = tk.Label(self.teacher_register_window, textvariable=self.alert_var_add, fg="red")        
        self.alert_label_add.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # register button
        register_button = tk.Button(self.teacher_register_window, text="Register", command=lambda:[self.register_button_clicked()])
        register_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # cancel button
        back_button = tk.Button(self.teacher_register_window, text="Back", command=lambda:[self.teacher_register_window.destroy()])
        back_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def save_button_clicked(self):
        self.alert_var.set("")
        if self.teacher_uid_entry.get() == "" or self.teacher_email_entry.get() == "" or self.teacher_password_entry.get() == "" or self.teacher_name_entry.get() == "":
            self.alert_var_edit.set("Please fill in all fields")
            return
        teacher_details = self.teacher_uid_entry.get() + "," + self.teacher_email_entry.get() + "," + self.teacher_password_entry.get() + "," + self.teacher_name_entry.get() + "," + self.teacher_course_entry.get() + ","
        if os.path.exists(self.teacher_path):
            with open(self.teacher_path, "r", encoding="utf-8") as rf:
                data = rf.readlines()
            data[self.selected_line] = teacher_details + "\n"
            with open(self.teacher_path, "w", encoding="utf-8") as wf:
                wf.writelines(data)
            self.load_teachers()
            self.alert_label_edit.config(fg="green")
            self.alert_var_edit.set("Teacher details updated")

    def register_button_clicked(self):
        pass
        uid = self.teacher_uid_entry.get()
        name = self.teacher_name_entry.get()
        email = self.teacher_email_entry.get()
        password = self.teacher_password_entry.get()

        if uid in self.tree.get_children():
            self.alert_label_add.config(fg="red")
            self.alert_var_add.set("UID already exists")
        elif uid == "" or name == "" or email == "" or password == "":
            self.alert_label_add.config(fg="red")
            self.alert_var_add.set("Please fill in all fields")
        elif email in self.tree.get_children():
            self.alert_label_add.config(fg="red")
            self.alert_var_add.set("Email already exists")
        elif "@" not in email or "." not in email:
            self.alert_label_add.config(fg="red")
            self.alert_var_add.set("Invalid email")
        else:
            self.register_teacher(uid, name, email, password)
            self.alert_label_add.config(fg="green")
            self.alert_var_add.set(f"Registration successful.")
            self.load_teachers()

    def register_teacher(self, tea_id, name, email, password, course="", status=""):
        if os.path.exists(self.teacher_path):
            with open(self.teacher_path, "a", encoding="utf8") as f:
                new_teacher = f"{tea_id},{email},{password},{name},{course},{status}"
                f.write(new_teacher + "\n")
            
    def activate_deactivate_teacher_button_clicked(self):
        selected_data = self.tree.focus()
        teacher_details = self.tree.item(selected_data, "values")
        if not selected_data:
            self.alert_label.config(fg="red")
            self.alert_var.set("Please select a Teacher")
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

    def back_to_home_button_clicked(self):
        self.master.hide_staff_staff_menu(self)
        self.master.show_staff_menu(self.staff_menu)
