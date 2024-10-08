import tkinter as tk
import os

class StaffStaffMenu(tk.Frame):
    def __init__(self, master, staff_user, staff_menu):
        super().__init__(master)
        self.master = master
        self.staff_user = staff_user
        self.staff_menu = staff_menu

        # all staff heading
        self.heading = tk.Label(self, text="All Staffs", font=("Arial", 18, "bold"))
        self.heading.pack(pady=20)

        # staff listbox
        self.staff_listbox = tk.Listbox(self, width=50, height=10)
        self.staff_listbox.pack(pady=20)
        self.load_staffs()

        # alert variable and label widget
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(self, textvariable=self.alert_var, font=("Arial", 12))
        self.alert_label.pack(pady=10)

        # edit staff button
        self.edit_staff_button = tk.Button(self, text="Edit Staff Details", command=self.edit_course_button_clicked)
        self.edit_staff_button.pack(pady=20)

        # back to home button
        self.back_to_home_button = tk.Button(self, text="Back to Home", command=self.back_to_home_button_clicked)
        self.back_to_home_button.pack(pady=10)

    def load_staffs(self):
        self.staff_listbox.delete(0, tk.END)
        all_staffs_path = "database/staff.txt"
        if os.path.exists(all_staffs_path):
            with open(all_staffs_path, "r", encoding="utf-8") as rf:
                lines = rf.readlines()
            for line in lines:
                self.staff_listbox.insert(tk.END, line.strip())

    def edit_course_button_clicked(self):
        # todo
        pass
            
    def back_to_home_button_clicked(self):
        self.master.hide_staff_staff_menu(self)
        self.master.show_staff_menu(self.staff_menu)
