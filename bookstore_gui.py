import tkinter as tk
from tkinter import messagebox
from bookstore_backend import connect, insertbook, viewstore, searchbook

# Function to add a book to the database
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    year = year_entry.get()
    isbn = isbn_entry.get()

    # Check if any field is empty
    if title == "" or author == "" or year == "" or isbn == "":
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Insert the book into the database
    insertbook(title, author, year, isbn)
    messagebox.showinfo("Success", "Book added successfully.")

# Function to view all books in the database
def view_books():
    books = viewstore()
    if not books:
        messagebox.showinfo("Info", "No books found.")
        return

    book_list.delete(0, tk.END)
    for book in books:
        book_list.insert(tk.END, f"{book[0]} - {book[1]} by {book[2]} ({book[3]})")

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

tk.Label(root, text="Year:").pack()
year_entry = tk.Entry(root)
year_entry.pack()

tk.Label(root, text="ISBN:").pack()
isbn_entry = tk.Entry(root)
isbn_entry.pack()

# Add Book Button
add_button = tk.Button(root, text="Add Book", command=add_book)
add_button.pack()

# View Books Button
view_button = tk.Button(root, text="View Books", command=view_books)
view_button.pack()

# Listbox to display books
book_list = tk.Listbox(root, height=10, width=50)
book_list.pack()

root.mainloop()
