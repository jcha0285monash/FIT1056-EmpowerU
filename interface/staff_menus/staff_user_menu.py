import tkinter as tk
from tkinter import ttk
import os
from app.student import Student
from app.teacher import Teacher
from app.staff import Staff

class StaffUserMenu(tk.Frame):
    def __init__(self, master, staff_user, staff_menu, user):
        super().__init__(master)
        self.master = master
        self.staff_user = staff_user
        self.staff_menu = staff_menu
        self.user = user
        # unique is the unique identifier for the user for the 4th column eg. course or role
        if self.user == "staff":
            self.unique = "Role"
        else:
            self.unique = "Course"

        style = ttk.Style()
        style.configure("Treeview", rowheight=47)  # Change row height to fit 3 courses

        # create tree view
        self.tree = ttk.Treeview(self, columns=("UID", "Email", "Password", "Name", self.unique, "Status"), show="headings")
        self.tree.heading("UID", text="UID")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Password", text="Password")
        self.tree.heading("Name", text="Name")
        self.tree.heading(self.unique, text=self.unique)
        self.tree.heading("Status", text="Status")

        # define column width and alignment
        self.tree.column("UID", width=100, anchor=tk.CENTER)
        self.tree.column("Email", width=150, anchor=tk.W)
        self.tree.column("Password", width=100, anchor=tk.W)
        self.tree.column("Name", width=150, anchor=tk.W)
        self.tree.column(self.unique, width=200, anchor=tk.W)
        self.tree.column("Status", width=85, anchor=tk.CENTER)

        # insert data into the table
        self.load_users()

        # all user heading
        self.heading = tk.Label(self, text=f"All {self.user.title()}s", font=("Arial", 18, "bold"))
        self.heading.grid(row=0, columnspan=4, padx=20, pady=10)

        # position the Treeview
        self.tree.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        # alert variable and label widget
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(self, textvariable=self.alert_var, font=("Arial", 12))
        self.alert_label.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        # edit user button
        self.edit_user_button = tk.Button(self, text=f"Edit {self.user.title()} Details", command=self.edit_user_button_clicked)
        self.edit_user_button.grid(row=3, column=0, padx=10, pady=10)

        # add user button
        self.add_user_button = tk.Button(self, text=f"Add {self.user.title()}", command=self.add_user_button_clicked)
        self.add_user_button.grid(row=3, column=1, padx=10, pady=10)

        # delete user button
        self.delete_user_button = tk.Button(self, text=f"Activate/Deactivate {self.user.title()}", command=self.activate_deactivate_user_button_clicked)
        self.delete_user_button.grid(row=3, column=2, padx=10, pady=10)

        # back to home button
        self.back_to_home_button = tk.Button(self, text="Back to Home", command=self.back_to_home_button_clicked)
        self.back_to_home_button.grid(row=3, column=3, padx=10, pady=10)

    def edit_user_button_clicked(self):
        selected_data = self.tree.focus()
        if not selected_data:
            self.alert_label.config(fg="red")
            self.alert_var.set(f"Please select a {self.user.title()}")
            return
        self.alert_var.set("")
        parent = self.tree.parent(selected_data)
        children = self.tree.get_children(parent)
        self.selected_line = children.index(selected_data)
        user_details = self.tree.item(selected_data, "values")
        self.selected_user_uid = user_details[0]
        self.selected_user_email = user_details[1]
        self.selected_user_password = user_details[2]
        self.selected_user_name = user_details[3]
        self.selected_user_unique = user_details[4]
        self.selected_user_status = user_details[5]
        user_edit_window = tk.Toplevel(self)
        user_edit_window.grab_set()
        user_edit_window.title(f"Edit user Details")
        user_edit_window.geometry("610x420")
        
        # user uid label
        user_uid_label = tk.Label(user_edit_window, text="user UID:", font=("Arial", 12))
        user_uid_label.grid(row=0, column=0, padx=10, pady=10)

        # user uid entry
        self.user_uid_edit_entry = tk.Entry(user_edit_window, width=50)
        self.user_uid_edit_entry.insert(0, self.selected_user_uid)
        self.user_uid_edit_entry.grid(row=0, column=1, padx=10, pady=10)

        # user email label
        user_email_label = tk.Label(user_edit_window, text="user Email:", font=("Arial", 12))
        user_email_label.grid(row=1, column=0, padx=10, pady=10)

        # user email entry
        self.user_email_edit_entry = tk.Entry(user_edit_window, width=50)
        self.user_email_edit_entry.insert(0, self.selected_user_email)
        self.user_email_edit_entry.grid(row=1, column=1, padx=10, pady=10)

        # user password label
        user_password_label = tk.Label(user_edit_window, text="user Password:", font=("Arial", 12))
        user_password_label.grid(row=2, column=0, padx=10, pady=10)

        # user password entry
        self.user_password_edit_entry = tk.Entry(user_edit_window, width=50)
        self.user_password_edit_entry.insert(0, self.selected_user_password)
        self.user_password_edit_entry.grid(row=2, column=1, padx=10, pady=10)

        # user name label
        user_name_label = tk.Label(user_edit_window, text="user Name:", font=("Arial", 12))
        user_name_label.grid(row=3, column=0, padx=10, pady=10)

        # user name entry
        self.user_name_edit_entry = tk.Entry(user_edit_window, width=50)
        self.user_name_edit_entry.insert(0, self.selected_user_name)
        self.user_name_edit_entry.grid(row=3, column=1, padx=10, pady=10)

        # user unique label
        user_unique_label = tk.Label(user_edit_window, text=f"{self.user.title()} {self.unique}:", font=("Arial", 12))
        user_unique_label.grid(row=4, column=0, padx=10, pady=10)

        # user unique text widget entry
        self.user_unique_edit_entry = tk.Text(user_edit_window, width=50, height=5)
        self.user_unique_edit_entry.insert(tk.END, self.selected_user_unique)
        self.user_unique_edit_entry.grid(row=4, column=1, padx=10, pady=10)

        # alert variable and label widget
        self.alert_var_edit = tk.StringVar()
        self.alert_label_edit = tk.Label(user_edit_window, textvariable=self.alert_var_edit, fg="red")        
        self.alert_label_edit.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # save button
        save_button = tk.Button(user_edit_window, text="Save", command=self.save_button_clicked)
        save_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # back button
        back_button = tk.Button(user_edit_window, text="Back", command=user_edit_window.destroy)
        back_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def add_user_button_clicked(self):
        self.selected_user_email = None
        self.selected_user_uid = None
        self.alert_var.set("")
        add_user_window = tk.Toplevel(self)
        add_user_window.grab_set()
        add_user_window.title(f"Add New user")
        add_user_window.geometry("610x410")

        # add new user heading
        add_new_user_heading = tk.Label(add_user_window, text=f"Add New {self.user.title()}", font=("Arial", 20))
        add_new_user_heading.grid(row=0, columnspan=2, padx=20, pady=10)

        # user uid label
        user_uid_label = tk.Label(add_user_window, text=f"{self.user.title()} UID:", font=("Arial", 12))
        user_uid_label.grid(row=1, column=0, padx=10, pady=10)

        # user uid entry
        self.user_uid_add_entry = tk.Entry(add_user_window, width=50)
        self.user_uid_add_entry.insert(0, self.user[:3] + str(len(self.tree.get_children()) + 1).zfill(4))
        self.user_uid_add_entry.grid(row=1, column=1, padx=10, pady=10)

        # user email variable label
        user_email_label = tk.Label(add_user_window, text=f"{self.user.title()} Email:", font=("Arial", 12))
        user_email_label.grid(row=2, column=0, padx=10, pady=10)

        # user email entry        
        self.user_email_add_entry = tk.Entry(add_user_window, width=50)
        self.user_email_add_entry.grid(row=2, column=1, padx=10, pady=10)

        # user password label
        user_password_label = tk.Label(add_user_window, text=f"{self.user.title()} Password:", font=("Arial", 12))
        user_password_label.grid(row=3, column=0, padx=10, pady=10)

        # user password entry
        self.user_password_add_entry = tk.Entry(add_user_window, width=50)
        self.user_password_add_entry.grid(row=3, column=1, padx=10, pady=10)

        # user name label
        user_name_label = tk.Label(add_user_window, text=f"{self.user.title()} Name:", font=("Arial", 12))
        user_name_label.grid(row=4, column=0, padx=10, pady=10)

        # user name entry
        self.user_name_add_entry = tk.Entry(add_user_window, width=50)
        self.user_name_add_entry.grid(row=4, column=1, padx=10, pady=10)

        # alert variable and label widget
        self.alert_var_add = tk.StringVar()
        self.alert_label_add = tk.Label(add_user_window, textvariable=self.alert_var_add, fg="red")        
        self.alert_label_add.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # add button
        add_button = tk.Button(add_user_window, text="add", command=self.add_button_clicked)
        add_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # cancel button
        back_button = tk.Button(add_user_window, text="Back", command=add_user_window.destroy)
        back_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def save_button_clicked(self):
        self.alert_var.set("")
        uid = self.user_uid_edit_entry.get()
        name = self.user_name_edit_entry.get()
        email = self.user_email_edit_entry.get()
        password = self.user_password_edit_entry.get()
        new_unique = self.user_unique_edit_entry.get("1.0", tk.END).strip().split("\n")

        # join "unique" data in text widget with &
        if len(new_unique) == 1:
            new_unique[0] += "&"
        unique = "&".join(new_unique)

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
        user_details = uid + "," + email + "," + password + "," + name + "," + unique + "," + self.selected_user_status
        if os.path.exists(self.user_path):
            with open(self.user_path, "r", encoding="utf-8") as rf:
                data = rf.readlines()
            data[self.selected_line] = user_details + "\n"
            with open(self.user_path, "w", encoding="utf-8") as wf:
                wf.writelines(data)
            self.load_users()
            self.alert_label_edit.config(fg="green")
            self.alert_var_edit.set(f"{self.user.title()} details updated")

    def add_button_clicked(self):
        uid = self.user_uid_add_entry.get()
        name = self.user_name_add_entry.get()
        email = self.user_email_add_entry.get()
        password = self.user_password_add_entry.get()

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
        self.add_user(uid, name, email, password)
        self.alert_label_add.config(fg="green")
        self.alert_var_add.set(f"Registration successful.")
        self.load_users()

    def add_user(self, uid, name, email, password, unique="", status=""):
        if os.path.exists(self.user_path):
            with open(self.user_path, "a", encoding="utf8") as f:
                new_user = f"{uid},{email},{password},{name},{unique},{status}"
                f.write(new_user + "\n")
            
    def activate_deactivate_user_button_clicked(self):
        selected_data = self.tree.focus()
        user_details = self.tree.item(selected_data, "values")
        if not selected_data:
            self.alert_label.config(fg="red")
            self.alert_var.set(f"Please select a {self.user}")
            return
        parent = self.tree.parent(selected_data)
        children = self.tree.get_children(parent)
        self.selected_line = children.index(selected_data)
        user_unique = user_details[4].replace("\n", "&")
        if user_details[5] == "DEACTIVATED":
            if os.path.exists(self.user_path):
                with open(self.user_path, "r", encoding="utf-8") as rf:
                    data = rf.readlines()
                data[self.selected_line] = user_details[0] + "," + user_details[1] + "," + user_details[2] + "," + user_details[3] + "," + user_unique + ",ACTIVE\n"
                with open(self.user_path, "w", encoding="utf-8") as wf:
                    wf.writelines(data)
                self.load_users()
                self.alert_label.config(fg="green")
                self.alert_var.set("Account activated")
                self.load_users
                return
        if os.path.exists(self.user_path):
            with open(self.user_path, "r", encoding="utf-8") as rf:
                data = rf.readlines()
            data[self.selected_line] = user_details[0] + "," + user_details[1] + "," + user_details[2] + "," + user_details[3] + "," + user_unique + ",DEACTIVATED\n"
            with open(self.user_path, "w", encoding="utf-8") as wf:
                wf.writelines(data)
            self.load_users()
            self.alert_label.config(fg="green")
            self.alert_var.set("Account deactivated")
            self.load_users
        
    def load_users(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.user_path = f"./database/{self.user}.txt"
        if os.path.exists(self.user_path):
            with open(self.user_path, "r", encoding="utf-8") as rf:
                lines = rf.readlines()
            for line in lines:
                values = line.strip().split(",")
                values[4] = values[4].replace("&", "\n")
                self.tree.insert("", tk.END, values=values)

    def import_user(self):
        user=[]
        if os.path.exists(self.user_path):
            with open(self.user_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            if self.user == "staff":
                for line in lines:
                    sta_id, email, password, name, role, status = line.strip().split(",")
                    user_obj = Staff(sta_id, email, password, name, role, status)
                    user.append(user_obj)
                return user
            elif self.user == "student":
                for line in lines:
                    stu_id, email, password, name, course, status = line.strip().split(",")
                    user_obj = Student(stu_id, email, password, name, course, status)
                    user.append(user_obj)
                return user
            elif self.user == "teacher":
                for line in lines:
                    tea_id, email, password, name, course, status = line.strip().split(",")
                    user_obj = Teacher(tea_id, email, password, name, course, status)
                    user.append(user_obj)
                return user

    def check_duplicate_uid(self, uid):
        imported = self.import_user()
        for user in imported:
            if user.uid == self.selected_user_uid:
                continue
            if user.uid == uid:
                return True
        return False

    def check_duplicate_email(self, email):
        imported = self.import_user()
        for user in imported:
            if user.email == self.selected_user_email:
                continue
            if user.email == email:
                return True
        return False

    def back_to_home_button_clicked(self):
        self.master.hide_staff_user_menu(self)
        self.master.show_staff_menu(self.staff_menu)