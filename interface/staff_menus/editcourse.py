import tkinter as tk
from tkinter import simpledialog, messagebox
import os
from interface.staff_menus.edittask import EditTaskContentPage

class EditCourseContentPage(tk.Frame):
    def __init__(self, master, selected_course, previous_menu):
        super().__init__(master)
        self.master = master
        self.selected_course = selected_course
        self.previous_menu = previous_menu

        # Course content heading
        self.heading = tk.Label(self, text=f"Editing Content for {selected_course}", font=("Arial", 18, "bold"))
        self.heading.pack(pady=20)

        # Course content text widget
        self.course_content_label = tk.Label(self, text="Course Content:")
        self.course_content_label.pack(pady=10)
        self.course_text = tk.Text(self, wrap=tk.WORD, width=60, height=10)
        self.course_text.pack(pady=10)
        self.load_course_content(selected_course)

        # Tasks listbox
        self.tasks_label = tk.Label(self, text="Course Tasks:")
        self.tasks_label.pack(pady=10)
        self.tasks_listbox = tk.Listbox(self, width=50, height=10)
        self.tasks_listbox.pack(pady=10)
        self.load_tasks(selected_course)

        
        self.add_task_button = tk.Button(self, text="Add New Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.add_task_button = tk.Button(self, text="Edit Task", command=self.edit_task)
        self.add_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(self, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        # "Edit Task Content" button to navigate to content editor
        self.edit_task_content_button = tk.Button(self, text="Edit Task Content", command=self.edit_task_content)
        self.edit_task_content_button.pack(pady=10)


        # Save and back buttons
        self.save_button = tk.Button(self, text="Save", command=self.save_content)
        self.save_button.pack(pady=5)

        self.back_button = tk.Button(self, text="Back", command=self.go_back)
        self.back_button.pack(pady=5)

    def load_course_content(self, selected_course):
        course_file_path = f"database/courses/{selected_course}.txt"
        self.course_text.delete(1.0, tk.END)
        if os.path.exists(course_file_path):
            with open(course_file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.course_text.insert(tk.END, content)
        else:
            self.course_text.insert(tk.END, f"No course content available for {selected_course}.")                

    def save_content(self):
        """Saves the modified course content and tasks."""
        course_file_path = f"database/courses/{self.selected_course}.txt"
        with open(course_file_path, "w", encoding="utf-8") as file:
            file.write(self.course_text.get(1.0, tk.END).strip())

        messagebox.showinfo("Save Successful", "Course content has been successfully saved.")

    def load_tasks(self, selected_course):
        self.tasks_listbox.delete(0, tk.END)
        tasks_directory = f"database/tasks/{selected_course}/"
        if not os.path.exists(tasks_directory):
            self.tasks_listbox.insert(tk.END, "Tasks directory not found.")
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
                self.tasks_listbox.insert(tk.END, display_text)

    def open_task(self):
        selected_task = self.tasks_listbox.get(tk.ACTIVE).split(" - ")[0]
        task_file_path = f"database/tasks/{self.selected_course}/{selected_task}.txt"
        self.course_text.delete(1.0, tk.END)

        if os.path.exists(task_file_path):
            with open(task_file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.course_text.insert(tk.END, content)
        else:
            self.course_text.insert(tk.END, f"No task content available for {selected_task}.")

    def edit_task(self):
        """Allows the staff to edit the selected task."""
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            selected_task = self.tasks_listbox.get(selected_task_index)
            new_task = simpledialog.askstring("Edit Task", "Enter the new task name:", initialvalue=selected_task)
            if new_task:
                selected_course = self.courses_listbox.get(tk.ACTIVE)
                self.update_task_in_file(selected_course, selected_task, new_task)

    def update_task_in_file(self, course_name, old_task, new_task):
        """Updates the task in the task file."""
        tasks_path = f"database/{course_name}_tasks.txt"
        with open(tasks_path, "r", encoding="utf-8") as rf:
            tasks = rf.readlines()
        tasks = [new_task + "\n" if task.strip() == old_task else task for task in tasks]

        with open(tasks_path, "w", encoding="utf-8") as wf:
            wf.writelines(tasks)

        self.load_tasks(None)

    def add_task(self):
        """Adds a new task to the selected course."""
        selected_task = self.tasks_listbox.get(tk.ACTIVE)
        if selected_task:
            new_task = simpledialog.askstring("New Task", f"Enter a new task for {selected_task}:")
            if new_task:
                tasks_path = f"database/tasks/{self.selected_course}/{selected_task}.txt"
                with open(tasks_path, "a", encoding="utf-8") as wf:
                    wf.write(new_task + "\n")
                self.load_tasks(None)

    def delete_task(self):
        """Deletes the selected task from the task file."""
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            selected_task = self.tasks_listbox.get(selected_task_index)
            confirmation = messagebox.askyesno("Delete Task", f"Are you sure you want to delete the task '{selected_task}'?")
            if confirmation:
                tasks_path = f"database/tasks/{self.selected_course}/{selected_task}.txt"
                with open(tasks_path, "r", encoding="utf-8") as rf:
                    tasks = rf.readlines()
                tasks = [task for task in tasks if task.strip() != selected_task]

                with open(tasks_path, "w", encoding="utf-8") as wf:
                    wf.writelines(tasks)

                self.load_tasks(None)

    def edit_task_content(self):
        """Opens a new page to edit the selected task."""
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            selected_task = self.tasks_listbox.get(selected_task_index)
            # Hide the current page and open the task edit page
            self.pack_forget()
            edit_task_page = EditTaskContentPage(self.master, self.selected_course, selected_task, self)
            edit_task_page.pack(fill="both", expand=True)            

    def go_back(self):
        """Returns to the previous menu."""
        self.pack_forget()
        self.master.show_staff_courses_menu(self.previous_menu)