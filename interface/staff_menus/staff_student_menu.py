import tkinter as tk
import os

class StaffStudentMenu(tk.Frame):
    def __init__(self, master, staff_user, staff_menu):
        super().__init__(master)
        self.master = master
        self.staff_user = staff_user
        self.staff_menu = staff_menu

        # all student heading
        self.heading = tk.Label(self, text="All Students", font=("Arial", 18, "bold"))
        self.heading.pack(pady=20)

        # student listbox
        self.student_listbox = tk.Listbox(self, width=50, height=10)
        self.student_listbox.pack(pady=20)
        self.load_students()

        # alert variable and label widget
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(self, textvariable=self.alert_var, font=("Arial", 12))
        self.alert_label.pack(pady=10)

        # edit student button
        self.edit_student_button = tk.Button(self, text="Edit Student Details", command=self.edit_student_button_clicked)
        self.edit_student_button.pack(pady=20)

        # back to home button
        self.back_to_home_button = tk.Button(self, text="Back to Home", command=self.back_to_home_button_clicked)
        self.back_to_home_button.pack(pady=10)

    def load_students(self):
        self.student_listbox.delete(0, tk.END)
        all_students_path = "database/student.txt"
        if os.path.exists(all_students_path):
            with open(all_students_path, "r", encoding="utf-8") as rf:
                lines = rf.readlines()
            for line in lines:
                self.student_listbox.insert(tk.END, line.strip())

    def edit_student_button_clicked(self):
        selected_indices = self.student_listbox.curselection()
        student_data = [self.student_listbox.get(i) for i in selected_indices]
        if not student_data:
            self.alert_label.config(fg="red")
            self.alert_var.set("Please select a student")
            return
        student_details = student_data[0]
        student_details = student_details.split(",")
        student_user_uid = student_details[0]
        student_user_email = student_details[1]
        student_user_password = student_details[2]
        student_user_name = student_details[3]
        student_user_course = student_details[4]
        student_edit_window = tk.Toplevel(self)
        student_edit_window.title(f"Edit Student Details")
        student_edit_window.geometry("610x350")
        
        # student uid label
        student_uid_label = tk.Label(student_edit_window, text="Student UID:", font=("Arial", 12))
        student_uid_label.grid(row=0, column=0, padx=10, pady=10)

        # student uid entry
        self.student_uid_entry = tk.Entry(student_edit_window, width=50)
        self.student_uid_entry.insert(0, student_user_uid)
        self.student_uid_entry.grid(row=0, column=1, padx=10, pady=10)

        # student email label
        student_email_label = tk.Label(student_edit_window, text="Student Email:", font=("Arial", 12))
        student_email_label.grid(row=1, column=0, padx=10, pady=10)

        # student email entry
        self.student_email_entry = tk.Entry(student_edit_window, width=50)
        self.student_email_entry.insert(0, student_user_email)
        self.student_email_entry.grid(row=1, column=1, padx=10, pady=10)

        # student password label
        student_password_label = tk.Label(student_edit_window, text="Student Password:", font=("Arial", 12))
        student_password_label.grid(row=2, column=0, padx=10, pady=10)

        # student password entry
        self.student_password_entry = tk.Entry(student_edit_window, width=50)
        self.student_password_entry.insert(0, student_user_password)
        self.student_password_entry.grid(row=2, column=1, padx=10, pady=10)

        # student name label
        student_name_label = tk.Label(student_edit_window, text="Student Name:", font=("Arial", 12))
        student_name_label.grid(row=3, column=0, padx=10, pady=10)

        # student name entry
        self.student_name_entry = tk.Entry(student_edit_window, width=50)
        self.student_name_entry.insert(0, student_user_name)
        self.student_name_entry.grid(row=3, column=1, padx=10, pady=10)

        # student course label
        student_course_label = tk.Label(student_edit_window, text="Student Course:", font=("Arial", 12))
        student_course_label.grid(row=4, column=0, padx=10, pady=10)

        # student course entry
        self.student_course_entry = tk.Entry(student_edit_window, width=50)
        self.student_course_entry.insert(0, student_user_course)
        self.student_course_entry.grid(row=4, column=1, padx=10, pady=10)

        # save button
        save_button = tk.Button(student_edit_window, text="Save", command=lambda:[self.save_button_clicked(),student_edit_window.destroy()])
        save_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # cancel button
        cancel_button = tk.Button(student_edit_window, text="Cancel", command=lambda:[student_edit_window.destroy()])
        cancel_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def save_button_clicked(self):
        student_details = self.student_uid_entry.get() + "," + self.student_email_entry.get() + "," + self.student_password_entry.get() + "," + self.student_name_entry.get() + "," + self.student_course_entry.get()
        selection = self.student_listbox.curselection()
        selection = selection[0]
        all_students_path = "database/student.txt"
        with open(all_students_path, "r", encoding="utf-8") as rf:
            data = rf.readlines()
        data[int(selection)] = student_details + "\n"
        with open(all_students_path, "w", encoding="utf-8") as wf:
            wf.writelines(data)
        self.load_students()
        pass
            
    def back_to_home_button_clicked(self):
        self.master.hide_staff_staff_menu(self)
        self.master.show_staff_menu(self.staff_menu)
