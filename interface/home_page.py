import tkinter as tk
from app.staff import Staff
from app.student import Student
from app.teacher import Teacher
from interface.staff_menu import StaffMenu
from interface.student_menu import StudentMenu
from interface.teacher_menu import TeacherMenu
from interface.register_menu import RegisterMenu

class HomePage(tk.Frame):
    def __init__(self, master, image_path):
        super().__init__(master=master)
        self.master = master
        self.image_path = image_path

        #logo image
        self.logo_photoimage = tk.PhotoImage(master=self, file=self.image_path)
        self.logo_label = tk.Label(master=self, image=self.logo_photoimage)
        self.logo_label.grid(row=0, columnspan=2, sticky=tk.S, padx=10, pady=10)        

        #welcome heading
        self.welcome_label = tk.Label(master=self, text="Welcome to EmpowerU", font=("Arial", 20))
        self.welcome_label.grid(row=1, columnspan=2, padx=10, pady=10)

        # Uid label widget
        self.uid_label = tk.Label(master=self, text="UID:")
        self.uid_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        # Uid variable and entry widget
        self.uid_var = tk.StringVar(master=self)
        self.uid_entry = tk.Entry(master=self, textvariable=self.uid_var)
        self.uid_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        # Password label widget
        self.password_label = tk.Label(master=self, text="Password:")
        self.password_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)

        # Password variable and entry widget
        self.password_var = tk.StringVar(master=self)
        self.password_entry = tk.Entry(master=self, textvariable=self.password_var, show="*")
        self.password_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        # Alert variable and label widget - displays alert messages where necessary
        self.alert_var = tk.StringVar(master=self)
        self.alert_label = tk.Label(master=self, textvariable=self.alert_var, fg="red")
        self.alert_label.grid(row=4, columnspan=2, padx=10, pady=10)

        # Login button widget
        self.login_button = tk.Button(master=self, text="Login", command=self.login_button_clicked)
        self.login_button.grid(row=5, columnspan=2, padx=10, pady=10)

        #register button widget
        self.register_button = tk.Button(master=self, text="Register", command=self.register_button_clicked)
        self.register_button.grid(row=6, columnspan=2, padx=10, pady=10)

        # Shut down button widget
        self.shutdown_button = tk.Button(master=self, text="Shut Down", command=master.destroy)
        self.shutdown_button.grid(row=7, columnspan=2, padx=10, pady=10)

    def login_button_clicked(self):
        # Get the entered UID and password
        uid = self.uid_var.get()
        password = self.password_var.get()

        if "stu" in uid:
            # If the entered UID is a student, create a Student object and call the login method
            student_user = Student.authenticate(uid, password)
            if isinstance(student_user, Student):
                # If the entered UID is a student, call the student_home method
                self.master.hide_homepage()
                studentmenu = StudentMenu(self.master, student_user)
                self.master.show_student_menu(studentmenu)
                self.clear_input()
        elif "tea" in uid:
            # If the entered UID is a teacher, create a Teacher object and call the login method
            teacher_user = Teacher.authenticate(uid, password)
            if isinstance(teacher_user, Teacher):
            # If the entered UID is a teacher, call the teacher_home method
                self.master.hide_homepage()
                teachermenu = TeacherMenu(self.master, teacher_user)
                self.master.show_teacher_menu(teachermenu)
                self.clear_input()
        elif "sta" in uid:
            # If the entered UID is a staff, create a Staff object and call the login method
            staff_user = Staff.authenticate(uid, password)
            if isinstance(staff_user, Staff):
                # If the entered UID is a staff, call the staff_home method
                self.master.hide_homepage()
                staffmenu = StaffMenu(self.master, staff_user)
                self.master.show_staff_menu(staffmenu)
                self.clear_input()
        else:
            # If the entered UID is not a valid user, display an error message
            self.alert_var.set("Invalid UID or Password")
            return
        
        # If the entered UID and password are valid, clear the entry fields
        self.alert_var.set("Invalid UID or Password")
        self.uid_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def clear_input(self):
        self.alert_var.set("")
        self.uid_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def register_button_clicked(self):
        registermenu = RegisterMenu(self.master, self)
        self.master.show_register_menu(registermenu)
        self.master.hide_homepage()