import tkinter as tk
from tkinter import messagebox
from bookstore_backend import connect, insertbook, viewstore, searchbook

# Function to add a book to the database
# Create the main window
root = tk.Tk()
root.title("Bookstore Application")

# Labels and Entry fields
tk.Label(root, text="Title:").pack()
title_entry = tk.Entry(root)
title_entry.pack()

tk.Label(root, text="Author:").pack()
author_entry = tk.Entry(root)
author_entry.pack()

# Listbox to display books
book_list = tk.Listbox(root, height=10, width=50)
book_list.pack()

root.mainloop()
