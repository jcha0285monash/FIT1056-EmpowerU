import tkinter as tk
from tkinter import messagebox
import os

class EditTaskContentPage(tk.Frame):
    def __init__(self, master, selected_course, selected_task, previous_menu):
        super().__init__(master)
        self.master = master
        self.selected_course = selected_course
        self.selected_task = selected_task.split(" - ")[0]  # Get task name without deadline
        self.previous_menu = previous_menu

        # Task content heading
        self.heading = tk.Label(self, text=f"Editing Task: {self.selected_task}", font=("Arial", 18, "bold"))
        self.heading.pack(pady=20)

        # Task content text widget
        self.task_content_label = tk.Label(self, text="Task Content:")
        self.task_content_label.pack(pady=10)
        self.task_text = tk.Text(self, wrap=tk.WORD, width=60, height=10)
        self.task_text.pack(pady=10)
        self.load_task_content()

        # Save and back buttons
        self.save_button = tk.Button(self, text="Save", command=self.save_task_content)
        self.save_button.pack(pady=5)

        self.back_button = tk.Button(self, text="Back", command=self.go_back)
        self.back_button.pack(pady=5)

    def load_task_content(self):
        """Loads the task content from a file."""
        task_file_path = f"database/tasks/{self.selected_course}/{self.selected_task}.txt"
        self.task_text.delete(1.0, tk.END)
        if os.path.exists(task_file_path):
            with open(task_file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.task_text.insert(tk.END, content)
        else:
            self.task_text.insert(tk.END, f"No task content available for {self.selected_task}.")

    def save_task_content(self):
        """Saves the modified task content."""
        task_file_path = f"database/tasks/{self.selected_course}/{self.selected_task}.txt"

        # Check if a file with the same task name already exists
        if os.path.exists(task_file_path):
            # If the file already exists, show a warning and prevent overwriting
            response = messagebox.askyesno("Task Exists", f"A task with the name '{self.selected_task}' already exists. Do you want to overwrite it?")
            if not response:
                return  # If the user chooses not to overwrite, exit the function

        # Save the new or updated task content
        with open(task_file_path, "w", encoding="utf-8") as file:
            file.write(self.task_text.get(1.0, tk.END).strip())

        messagebox.showinfo("Save Successful", "Task content has been successfully saved.")


    def go_back(self):
        """Returns to the previous menu."""
        self.pack_forget()
        self.previous_menu.pack(fill="both", expand=True)
