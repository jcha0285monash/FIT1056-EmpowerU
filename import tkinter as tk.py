import tkinter as tk

def get_selected_value(event):
    # Get the index of the selected item(s)
    selected_indices = listbox.curselection()
    selected_values = [listbox.get(i) for i in selected_indices]
    print("Selected value(s):", selected_values)

# Create the main window
root = tk.Tk()
root.title("Tkinter Listbox Example")

# Create a Listbox
listbox = tk.Listbox(root, selectmode=tk.SINGLE)  # or selectmode=tk.MULTIPLE for multiple selections
listbox.pack()

# Add items to the Listbox
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
for item in items:
    listbox.insert(tk.END, item)

# Bind the event to detect selection
listbox.bind("<<ListboxSelect>>", get_selected_value)

# Start the Tkinter main loop
root.mainloop()
