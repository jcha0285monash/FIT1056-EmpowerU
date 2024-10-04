import tkinter as tk

class TeacherMenu(tk.Frame):
    def __init__(self, master, teacher_user):
        super().__init__(master)
        self.master = master        
        self.teacher_user = teacher_user

        #teacher heading
        self.teacher_heading = tk.Label(self, text="Teacher Menu", font=("Arial", 16))
        self.teacher_heading.pack(pady=20)

    def show_menu(self):
        self.place(relx=0.5, rely=0.5, anchor=tk.CENTER)