import tkinter as tk
from tkinter import ttk, messagebox
from Automation import export_and_clear_chat  # Importing the function directly

# File to store usernames
filename = "usernames.txt"

def load_usernames():
    try:
        with open(filename, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        messagebox.showwarning("File Error", "Usernames file not found!")
        return []

def show_usernames():
    usernames = load_usernames()
    listbox.delete(0, tk.END)  # Clear the listbox before showing the usernames
    if usernames:
        for username in usernames:
            listbox.insert(tk.END, username)  # Display usernames in the listbox
    else:
        listbox.insert(tk.END, "No usernames found.")

def process_selected_groups():
    selected_indices = listbox.curselection()
    if selected_indices:
        selected_usernames = [listbox.get(i) for i in selected_indices]
        print("Processing selected groups:")
        for username in selected_usernames:
            print(f"Processing group: {username}")
            export_and_clear_chat(username)
        print("Processing completed.")
    else:
        print("No usernames selected.")

# Setting up the main application window
root = tk.Tk()
root.title("Group Name Viewer")

# Set window size
window_width = 550
window_height = 600

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position to center the window
position_x = (screen_width // 2) - (window_width // 2)
position_y = (screen_height // 2) - (window_height // 2)

# Set the geometry of the window
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

# Setting up the theme
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TLabel", font=("Helvetica", 14))

# Header label
header_label = ttk.Label(root, text="List of Usernames", font=("Helvetica", 16, "bold"))
header_label.grid(row=0, column=0, padx=10, pady=10, sticky="EW")

# Frame for displaying usernames
list_frame = ttk.Frame(root, padding="10 10 10 10")
list_frame.grid(row=1, column=0, padx=10, pady=10, sticky="EW")

# Create the Listbox with MULTIPLE selection mode
listbox = tk.Listbox(list_frame, height=20, width=50, font=("Helvetica", 12), selectmode=tk.MULTIPLE)
listbox.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=listbox.yview)
scrollbar.pack(side="right", fill="y")

listbox.config(yscrollcommand=scrollbar.set)

# Frame for the action buttons
action_frame = ttk.Frame(root, padding="20 20 20 20")
action_frame.grid(row=2, column=0, padx=10, pady=10, sticky="EW")

# Button to process the selected groups and run the script
select_button = ttk.Button(action_frame, text="Process Selected Groups", command=process_selected_groups)
select_button.grid(row=0, column=0, padx=5, pady=5, sticky="EW")

# Load and display usernames on startup
show_usernames()

# Run the application
root.mainloop()
