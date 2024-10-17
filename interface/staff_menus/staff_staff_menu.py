import tkinter as tk
from tkinter import ttk
import os

class StaffStaffMenu(tk.Frame):
    def __init__(self, master, staff_user, staff_menu):
        super().__init__(master)
        super().__init__(master)
        self.master = master
        self.staff_user = staff_user
        self.staff_menu = staff_menu

        # create tree view
        self.tree = ttk.Treeview(self, columns=("UID", "Email", "Password", "Name", "Role", "Status"), show="headings")
        self.tree.heading("UID", text="UID")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Password", text="Password")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Role", text="Role")
        self.tree.heading("Status", text="Status")

        # define column width and alignment
        self.tree.column("UID", width=100, anchor=tk.CENTER)
        self.tree.column("Email", width=150, anchor=tk.W)
        self.tree.column("Password", width=100, anchor=tk.W)
        self.tree.column("Name", width=150, anchor=tk.W)
        self.tree.column("Role", width=100, anchor=tk.W)
        self.tree.column("Status", width=100, anchor=tk.W)

        # insert data into the table
        self.load_staffs()

        # all staff heading
        self.heading = tk.Label(self, text="All Staffs", font=("Arial", 18, "bold"))
        self.heading.pack(pady=20)

        # position the Treeview
        self.tree.pack(pady=10)

        # alert variable and label widget
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(self, textvariable=self.alert_var, font=("Arial", 12))
        self.alert_label.pack(pady=10)

        # edit staff button
        self.edit_staff_button = tk.Button(self, text="Edit Staff Details", command=self.edit_staff_button_clicked)
        self.edit_staff_button.pack(pady=10)

        # add staff button
        self.add_staff_button = tk.Button(self, text="Add Staff", command=self.add_staff_button_clicked)
        self.add_staff_button.pack(pady=10)

        # delete staff button
        self.delete_staff_button = tk.Button(self, text="Activate/Deactivate Staff", command=self.activate_deactivate_staff_button_clicked)
        self.delete_staff_button.pack(pady=10)

        # back to home button
        self.back_to_home_button = tk.Button(self, text="Back to Home", command=self.back_to_home_button_clicked)
        self.back_to_home_button.pack(pady=10)

    def edit_staff_button_clicked(self):
        selected_data = self.tree.focus()
        if not selected_data:
            self.alert_label.config(fg="red")
            self.alert_var.set("Please select a staff")
            return
        self.alert_var.set("")
        parent = self.tree.parent(selected_data)
        children = self.tree.get_children(parent)
        self.selected_line = children.index(selected_data)
        staff_details = self.tree.item(selected_data, "values")
        staff_user_uid = staff_details[0]
        staff_user_email = staff_details[1]
        staff_user_password = staff_details[2]
        staff_user_name = staff_details[3]
        staff_user_role = staff_details[4]
        self.staff_edit_window = tk.Toplevel(self)
        self.staff_edit_window.title(f"Edit Staff Details")
        self.staff_edit_window.geometry("610x390")
        
        # staff uid label
        staff_uid_label = tk.Label(self.staff_edit_window, text="Staff UID:", font=("Arial", 12))
        staff_uid_label.grid(row=0, column=0, padx=10, pady=10)

        # staff uid entry
        self.staff_uid_entry = tk.Entry(self.staff_edit_window, width=50)
        self.staff_uid_entry.insert(0, staff_user_uid)
        self.staff_uid_entry.grid(row=0, column=1, padx=10, pady=10)

        # staff email label
        staff_email_label = tk.Label(self.staff_edit_window, text="Staff Email:", font=("Arial", 12))
        staff_email_label.grid(row=1, column=0, padx=10, pady=10)

        # staff email entry
        self.staff_email_entry = tk.Entry(self.staff_edit_window, width=50)
        self.staff_email_entry.insert(0, staff_user_email)
        self.staff_email_entry.grid(row=1, column=1, padx=10, pady=10)

        # staff password label
        staff_password_label = tk.Label(self.staff_edit_window, text="Staff Password:", font=("Arial", 12))
        staff_password_label.grid(row=2, column=0, padx=10, pady=10)

        # staff password entry
        self.staff_password_entry = tk.Entry(self.staff_edit_window, width=50)
        self.staff_password_entry.insert(0, staff_user_password)
        self.staff_password_entry.grid(row=2, column=1, padx=10, pady=10)

        # staff name label
        staff_name_label = tk.Label(self.staff_edit_window, text="Staff Name:", font=("Arial", 12))
        staff_name_label.grid(row=3, column=0, padx=10, pady=10)

        # staff name entry
        self.staff_name_entry = tk.Entry(self.staff_edit_window, width=50)
        self.staff_name_entry.insert(0, staff_user_name)
        self.staff_name_entry.grid(row=3, column=1, padx=10, pady=10)

        # staff role label
        staff_role_label = tk.Label(self.staff_edit_window, text="Staff role:", font=("Arial", 12))
        staff_role_label.grid(row=4, column=0, padx=10, pady=10)

        # staff role entry
        self.staff_role_entry = tk.Entry(self.staff_edit_window, width=50)
        self.staff_role_entry.insert(0, staff_user_role)
        self.staff_role_entry.grid(row=4, column=1, padx=10, pady=10)

        # alert variable and label widget
        self.alert_var_edit = tk.StringVar()
        self.alert_label_edit = tk.Label(self.staff_edit_window, textvariable=self.alert_var_edit, fg="red")        
        self.alert_label_edit.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # save button
        save_button = tk.Button(self.staff_edit_window, text="Save", command=self.save_button_clicked)
        save_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # back button
        back_button = tk.Button(self.staff_edit_window, text="Back", command=self.staff_edit_window.destroy)
        back_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def load_staffs(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.staff_path = "database/staff.txt"
        if os.path.exists(self.staff_path):
            with open(self.staff_path, "r", encoding="utf-8") as rf:
                lines = rf.readlines()
            for line in lines:
                self.tree.insert("", tk.END, values=line.strip().split(","))

    def add_staff_button_clicked(self):
        self.alert_var.set("")
        self.staff_register_window = tk.Toplevel(self)
        self.staff_register_window.title(f"Add New Staff")
        self.staff_register_window.geometry("610x410")

        # add new staff heading
        self.add_new_staff_heading = tk.Label(self.staff_register_window, text="Add New Staff", font=("Arial", 20))
        self.add_new_staff_heading.grid(row=0, columnspan=2, padx=20, pady=10)

        # staff uid label
        staff_uid_label = tk.Label(self.staff_register_window, text="Staff UID:", font=("Arial", 12))
        staff_uid_label.grid(row=1, column=0, padx=10, pady=10)

        # staff uid entry
        self.staff_uid_entry = tk.Entry(self.staff_register_window, width=50)
        self.staff_uid_entry.insert(0, "sta" + str(len(self.tree.get_children()) + 1).zfill(4))
        self.staff_uid_entry.grid(row=1, column=1, padx=10, pady=10)

        # staff email variable label
        staff_email_label = tk.Label(self.staff_register_window, text="Staff Email:", font=("Arial", 12))
        staff_email_label.grid(row=2, column=0, padx=10, pady=10)

        # staff email entry        
        self.staff_email_entry = tk.Entry(self.staff_register_window, width=50)
        self.staff_email_entry.grid(row=2, column=1, padx=10, pady=10)

        # staff password label
        staff_password_label = tk.Label(self.staff_register_window, text="Staff Password:", font=("Arial", 12))
        staff_password_label.grid(row=3, column=0, padx=10, pady=10)

        # staff password entry
        self.staff_password_entry = tk.Entry(self.staff_register_window, width=50)
        self.staff_password_entry.grid(row=3, column=1, padx=10, pady=10)

        # staff name label
        staff_name_label = tk.Label(self.staff_register_window, text="Staff Name:", font=("Arial", 12))
        staff_name_label.grid(row=4, column=0, padx=10, pady=10)

        # staff name entry
        self.staff_name_entry = tk.Entry(self.staff_register_window, width=50)
        self.staff_name_entry.grid(row=4, column=1, padx=10, pady=10)

        # alert variable and label widget
        self.alert_var_add = tk.StringVar()
        self.alert_label_add = tk.Label(self.staff_register_window, textvariable=self.alert_var_add, fg="red")        
        self.alert_label_add.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # register button
        register_button = tk.Button(self.staff_register_window, text="Register", command=self.register_button_clicked)
        register_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # cancel button
        back_button = tk.Button(self.staff_register_window, text="Back", command=lambda:[self.staff_register_window.destroy()])
        back_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def save_button_clicked(self):
        self.alert_var_edit.set("")
        if self.staff_uid_entry.get() == "" or self.staff_email_entry.get() == "" or self.staff_password_entry.get() == "" or self.staff_name_entry.get() == "":
            self.alert_var_edit.set("Please fill in all fields")
            return
        staff_details = self.staff_uid_entry.get() + "," + self.staff_email_entry.get() + "," + self.staff_password_entry.get() + "," + self.staff_name_entry.get() + "," + self.staff_role_entry.get() + ","
        if os.path.exists(self.staff_path):
            with open(self.staff_path, "r", encoding="utf-8") as rf:
                data = rf.readlines()
            data[self.selected_line] = staff_details + "\n"
            with open(self.staff_path, "w", encoding="utf-8") as wf:
                wf.writelines(data)
            self.load_staffs()
            self.alert_label_edit.config(fg="green")
            self.alert_var_edit.set("Staff details updated")

    def register_button_clicked(self):
        pass
        uid = self.staff_uid_entry.get()
        name = self.staff_name_entry.get()
        email = self.staff_email_entry.get()
        password = self.staff_password_entry.get()

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
            self.register_staff(uid, name, email, password)
            self.alert_label_add.config(fg="green")
            self.alert_var_add.set(f"Registration successful.")
            self.load_staffs()

    def register_staff(self, sta_id, name, email, password, role="", status=""):
        if os.path.exists(self.staff_path):
            with open(self.staff_path, "a", encoding="utf8") as f:
                new_staff = f"{sta_id},{email},{password},{name},{role},{status}"
                f.write(new_staff + "\n")
            
    def activate_deactivate_staff_button_clicked(self):
        selected_data = self.tree.focus()
        staff_details = self.tree.item(selected_data, "values")
        if not selected_data:
            self.alert_label.config(fg="red")
            self.alert_var.set("Please select a staff")
            return
        parent = self.tree.parent(selected_data)
        children = self.tree.get_children(parent)
        self.selected_line = children.index(selected_data)
        if staff_details[5] == "DEACTIVATED":
            if os.path.exists(self.staff_path):
                with open(self.staff_path, "r", encoding="utf-8") as rf:
                    data = rf.readlines()
                data[self.selected_line] = staff_details[0] + "," + staff_details[1] + "," + staff_details[2] + "," + staff_details[3] + "," + staff_details[4] + ",\n"
                with open(self.staff_path, "w", encoding="utf-8") as wf:
                    wf.writelines(data)
                self.load_staffs()
                self.alert_label.config(fg="green")
                self.alert_var.set("Account activated")
                self.load_staffs
                return
        if os.path.exists(self.staff_path):
            with open(self.staff_path, "r", encoding="utf-8") as rf:
                data = rf.readlines()
            data[self.selected_line] = staff_details[0] + "," + staff_details[1] + "," + staff_details[2] + "," + staff_details[3] + "," + staff_details[4] + ",DEACTIVATED\n"
            with open(self.staff_path, "w", encoding="utf-8") as wf:
                wf.writelines(data)
            self.load_staffs()
            self.alert_label.config(fg="green")
            self.alert_var.set("Account deactivated")
            self.load_staffs
 
    def back_to_home_button_clicked(self):
        self.master.hide_staff_staff_menu(self)
        self.master.show_staff_menu(self.staff_menu)
