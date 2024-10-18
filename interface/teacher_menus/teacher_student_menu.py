import tkinter as tk
from tkinter import ttk
import os

class TeacherStudentMenu(tk.Frame):
    def __init__(self, master, teacher_user, teacher_menu):
        super().__init__(master)
        self.master = master
        self.teacher_user = teacher_user
        self.teacher_menu = teacher_menu

        # create tree view
        self.tree = ttk.Treeview(self, columns=("UID", "Email", "Password", "Name", "Course"), show="headings")
        self.tree.heading("UID", text="UID")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Password", text="Password")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Course", text="Course")

        # define column width and alignment
        self.tree.column("UID", width=100, anchor=tk.CENTER)
        self.tree.column("Email", width=150, anchor=tk.W)
        self.tree.column("Password", width=100, anchor=tk.W)
        self.tree.column("Name", width=150, anchor=tk.W)
        self.tree.column("Course", width=100, anchor=tk.W)

        # insert data into the table
        self.load_students()

        # all student heading
        self.heading = tk.Label(self, text="All Students", font=("Arial", 18, "bold"))
        self.heading.pack(pady=20)

        # position the Treeview
        self.tree.pack(pady=10)

        # alert variable and label widget
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(self, textvariable=self.alert_var, font=("Arial", 12))
        self.alert_label.pack(pady=10)

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
                self.tree.insert("", tk.END, values=line.strip().split(","))


    def back_to_home_button_clicked(self):
        self.pack_forget()
        self.teacher_menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
