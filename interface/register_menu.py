import tkinter as tk
from app.student import Student
import os

class RegisterMenu(tk.Frame):
    def __init__(self, master, homepage):
        super().__init__(master)
        self.master = master
        self.homepage = homepage

        #register heading
        self.heading = tk.Label(self, text="Register as New Student", font=("Arial", 20))
        self.heading.grid(row=0, columnspan=2, padx=20, pady=20)

        # name label widget
        self.name_label = tk.Label(master=self, text="Name:")
        self.name_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

        # name variable and entry widget
        self.name_var = tk.StringVar()
        self.name_entry = tk.Entry(master=self, textvariable=self.name_var)
        self.name_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        # email label widget
        self.email_label = tk.Label(master=self, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        # email variable and entry widget
        self.email_var = tk.StringVar()
        self.email_entry = tk.Entry(master=self, textvariable=self.email_var)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        # password label widget
        self.password_label = tk.Label(master=self, text="Password:")
        self.password_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)

        # password entry widget
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(master=self, textvariable=self.password_var, show="*")
        self.password_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        # confirm password label widget
        self.confirm_password_label = tk.Label(master=self, text="Confirm Password:")
        self.confirm_password_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.E)

        # confirm password variable and entry widget
        self.confirm_password_var = tk.StringVar()
        self.confirm_password_entry = tk.Entry(master=self, textvariable=self.confirm_password_var, show="*")
        self.confirm_password_entry.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)

        # alert variable and label widget
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(master=self, textvariable=self.alert_var, fg="red")
        self.alert_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # register button widget
        self.register_button = tk.Button(master=self, text="Register", command=self.register_button_clicked)        
        self.register_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        # back to homepage button widget
        self.back_button = tk.Button(master=self, text="Back to Homepage", command=self.back_to_homepage_button_clicked)
        self.back_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def register_button_clicked(self):
        name = self.name_var.get()
        email = self.email_var.get()
        password = self.password_var.get()
        confirm_password = self.confirm_password_var.get()

        if password != confirm_password:
            self.alert_label.config(fg="red")
            self.alert_var.set("Passwords do not match")
        elif name == "" or email == "" or password == "" or confirm_password == "":
            self.alert_label.config(fg="red")
            self.alert_var.set("Please fill in all fields")
        elif self.validate_email(email):
            self.alert_label.config(fg="red")
            self.alert_var.set("Email already exists")
        elif "@" not in email or "." not in email:
            self.alert_label.config(fg="red")
            self.alert_var.set("Invalid email")
        else:
            stu_id = self.register_student(name, email, password)
            self.alert_label.config(fg="green")
            self.alert_var.set(f"Registration successful.\nPlease log in with uid {stu_id}.")

    def import_students(self):
        self.students=[]
        student_path = "./database/student.txt"
        if os.path.exists(student_path):
            with open(student_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                stu_id, email, password, name, course, status = line.strip().split(",")
                student_obj = Student(stu_id, email, password, name, course, status)
                self.students.append(student_obj)
            return self.students

    def register_student(self, name, email, password, course="", status="ACTIVE"):
        student_path = "./database/student.txt"
        stu_id = "stu" + str(len(self.students) + 1).zfill(4)
        if os.path.exists(student_path):
            with open(student_path, "a", encoding="utf8") as f:
                new_student = f"{stu_id},{email},{password},{name},{course},{status}"
                f.write(new_student + "\n")
            return stu_id

    def validate_email(self, email):
        self.import_students()
        for student in self.students:
            if student.email == email:
                return True
        return False

    def back_to_homepage_button_clicked(self):
        self.master.show_homepage()
        self.master.hide_register_menu(self)