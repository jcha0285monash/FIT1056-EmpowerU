import tkinter as tk
from tkinter import ttk
import os
from datetime import datetime

class CourseDetailsPage(tk.Frame):
    def __init__(self, master, selected_course, student_user, student_menu):
        super().__init__(master)
        self.master = master
        self.selected_course = selected_course
        self.student_user = student_user
        self.student_menu = student_menu

        # Course name heading
        self.heading = tk.Label(self, text=f"Course Details: {selected_course}", font=("Arial", 16, "bold"))
        self.heading.pack(pady=20)

        # Progress bar for the course
        self.progress_bar = ttk.Progressbar(self, length=400, mode='determinate', maximum=100)
        self.progress_bar.pack(pady=10)
        self.progress_label = tk.Label(self, text="Progress: 0%")
        self.progress_label.pack()

        # Course content text widget
        self.course_text = tk.Text(self, wrap=tk.WORD, width=60, height=15, font=("Arial", 12))
        self.course_text.pack(pady=20)
        self.load_course_content(selected_course)

        # Outstanding tasks listbox
        self.task_label = tk.Label(self, text="Outstanding Tasks")
        self.task_label.pack()
        self.task_listbox = tk.Listbox(self, width=50, height=10)
        self.task_listbox.pack(pady=20)
        self.load_tasks(selected_course)
        
        self.alert_var = tk.StringVar()
        self.alert_label = tk.Label(self, textvariable=self.alert_var, fg="red", font=("Arial", 12))
        self.alert_label.pack(pady=10)

        button_frame = tk.Frame(self)
        button_frame.pack(fill="x", pady=10)

        # "Open Task" button
        self.select_task_button = tk.Button(button_frame, text="Open Task", command=self.open_task)
        self.select_task_button.grid(row=0, column=4, padx=5, pady=5, sticky="W")

        # "Back to Course" button
        self.back_button = tk.Button(button_frame, text="Back to Course", command=self.load_course_content_button)
        self.back_button.grid(row=0, column=5, padx=5, pady=5, sticky="E")

        # "Back to Home" button
        self.back_button = tk.Button(button_frame, text="Back to Home", command=self.back_to_home)
        self.back_button.grid(row=0, column=6, padx=5, pady=5, sticky="E")

        # "Mark as Done" button (initially hidden)
        self.markdone_button = tk.Button(button_frame, text="Mark Task as Done", command=self.markdone)
        self.markdone_button.grid(row=0, column=7, padx=5, pady=5, sticky="E")
        self.markdone_button.grid_remove()

        # Calculate initial progress after setting up UI components
        self.calculate_progress()

    def load_course_content(self, selected_course):
        course_file_path = f"database/courses/{selected_course}.txt"
        self.course_text.delete(1.0, tk.END)
        if os.path.exists(course_file_path):
            with open(course_file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.course_text.insert(tk.END, content)
        else:
            self.course_text.insert(tk.END, f"No course content available for {selected_course}.")

    def load_course_content_button(self):
        self.load_course_content(self.selected_course)

    def load_tasks(self, selected_course):
        self.task_listbox.delete(0, tk.END)
        tasks_directory = f"database/tasks/{selected_course}/"
        if not os.path.exists(tasks_directory):
            self.task_listbox.insert(tk.END, "Tasks directory not found.")
            return

        for task_file in os.listdir(tasks_directory):
            if task_file.endswith(".txt"):
                task_name = os.path.splitext(task_file)[0]
                task_file_path = os.path.join(tasks_directory, task_file)
                deadline_str = "No deadline specified"
                
                try:
                    with open(task_file_path, "r", encoding="utf-8") as file:
                        for line in file:
                            if line.lower().startswith("deadline:"):
                                deadline_str = line.split(":", 1)[1].strip()
                                break
                except Exception as e:
                    print(f"Error reading file {task_file}: {e}")

                display_text = f"{task_name} - {deadline_str}"
                self.task_listbox.insert(tk.END, display_text)

    def open_task(self):
        if self.task_listbox.curselection():
            selected_task = self.task_listbox.get(tk.ACTIVE).split(" - ")[0]
            task_file_path = f"database/tasks/{self.selected_course}/{selected_task}.txt"
            self.course_text.delete(1.0, tk.END)
            if selected_task:
                if os.path.exists(task_file_path):
                    with open(task_file_path, "r", encoding="utf-8") as file:
                        content = file.read()
                        self.course_text.insert(tk.END, content)
                        
                        
                        self.alert_var.set("")
                        # Show the "Mark as Done" button only if the task isn't already marked as done
                        if "Done" not in content:
                            self.markdone_button.grid(row=0, column=7, padx=5, pady=5, sticky="W")
                        else:
                            self.markdone_button.grid_remove()
                else:
                    self.course_text.insert(tk.END, f"No task content available for {selected_task}.")
            else:
                # Show an alert if no task is selected
                self.alert_var.set("Please select a task to view its content.")
        else:
        # Show an alert if no task is selected
            self.alert_var.set("Please select a task to view its content.")    

    def calculate_progress(self):
        tasks_directory = f"database/tasks/{self.selected_course}/"
        completed_tasks = 0

        # Check if the tasks directory exists and has tasks
        if not os.path.exists(tasks_directory):
            self.progress_bar['value'] = 0
            self.progress_label.config(text="Progress: 0%")
            return 0

        # Loop through each task file
        task_files = [file for file in os.listdir(tasks_directory) if file.endswith(".txt")]
        total_tasks = len(task_files)

        for task_file in task_files:
            task_file_path = os.path.join(tasks_directory, task_file)
            with open(task_file_path, "r", encoding="utf-8") as file:
                content = file.read()
                if "Done" in content:
                    completed_tasks += 1

        # Calculate the progress based on completed tasks
        progress = int((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0
        self.progress_bar['value'] = progress
        self.progress_label.config(text=f"Progress: {progress}%")
        return progress


    def markdone(self):
        selected_task = self.task_listbox.get(tk.ACTIVE).split(" - ")[0]
        task_file_path = f"database/tasks/{self.selected_course}/{selected_task}.txt"

        if os.path.exists(task_file_path):
            with open(task_file_path, "r+", encoding="utf-8") as file:
                content = file.read()
                if "Done" not in content:
                    file.write("\nDone")
                    # Update the progress bar and remove the button
                    
                    self.markdone_button.grid_remove()

        self.calculate_progress()            

    def back_to_home(self):
        self.pack_forget()
        self.master.show_student_menu(self.student_menu)

