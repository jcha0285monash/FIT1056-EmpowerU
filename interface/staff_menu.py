import tkinter as tk

class StaffMenu(tk.Frame):
    def __init__(self, master, staff_user):
        super().__init__(master)
        self.master = master
        self.staff_user = staff_user

        # Staff Heading
        self.staff_heading = tk.Label(self, text="Staff Menu", font=("Arial", 20, "bold"))
        self.staff_heading.pack(pady=20)

    def show_menu(self):
        self.place(relx=0.5, rely=0.5, anchor=tk.CENTER)