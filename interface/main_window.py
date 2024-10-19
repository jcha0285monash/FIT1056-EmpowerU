import tkinter as tk
from interface.home_page import HomePage

class EmpowerU(tk.Tk):
    def __init__(self, title, width, height):
        super().__init__()
        super().title(title)
        super().geometry(f"{width}x{height}")

        self.homepage = HomePage(master=self, image_path="./images/logo.png")
        self.show_homepage()

    def show_homepage(self):
        self.homepage.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def hide_homepage(self):
        self.homepage.place_forget()

    def show_register_menu(self, registermenu):
        register_menu = registermenu
        register_menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def hide_register_menu(self, registermenu):
        register_menu = registermenu
        register_menu.place_forget()

    def show_student_menu(self, studentmenu):
        student_menu = studentmenu
        student_menu.load_courses()
        student_menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def hide_student_menu(self, studentmenu):
        student_menu = studentmenu
        student_menu.place_forget()

    def show_staff_menu(self, staffmenu):
        staff_menu = staffmenu
        staff_menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def hide_staff_menu(self, staffmenu):
        staff_menu = staffmenu
        staff_menu.place_forget()

    def show_teacher_menu(self, teachermenu):
        teacher_menu = teachermenu
        teacher_menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def hide_teacher_menu(self, teachermenu):
        teacher_menu = teachermenu
        teacher_menu.place_forget()

    def show_available_courses_menu(self, availablecoursesmenu):
        available_courses_menu = availablecoursesmenu
        available_courses_menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    def hide_available_courses_menu(self, availablecoursesmenu):
        available_courses_menu = availablecoursesmenu
        available_courses_menu.place_forget()

    def show_staff_courses_menu(self, staffcoursesmenu):
        staff_courses_menu = staffcoursesmenu
        staff_courses_menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def hide_staff_courses_menu(self, staffcoursesmenu):
        staff_courses_menu = staffcoursesmenu
        staff_courses_menu.place_forget()

    def show_staff_staff_menu(self, staffstaffmenu):
        staff_staff_menu = staffstaffmenu
        staff_staff_menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def hide_staff_staff_menu(self, staffstaffmenu):
        staff_staff_menu = staffstaffmenu
        staff_staff_menu.place_forget()

    def show_staff_student_menu(self, staffstudentmenu):
        staff_student_menu = staffstudentmenu
        staff_student_menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def hide_staff_student_menu(self, staffstudentmenu):
        staff_student_menu = staffstudentmenu
        staff_student_menu.place_forget()

    def show_staff_teacher_menu(self, staffteachermenu):
        staff_teacher_menu = staffteachermenu
        staff_teacher_menu.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def hide_staff_teacher_menu(self, staffteachermenu):
        staff_teacher_menu = staffteachermenu
        staff_teacher_menu.place_forget()