import tkinter as tk
from tkinter import ttk, messagebox, font
import openpyxl
from openpyxl import Workbook
import pathlib
from PIL import Image, ImageTk

def create_excel_if_not_exists():
    file = pathlib.Path('barber_shop_data.xlsx')
    if not file.exists():
        wb = Workbook()
        ws = wb.active
        ws.append(["Name", "Phone Number", "Age", "Sex", "Email Address", "Inquiry"])
        wb.save('barber_shop_data.xlsx')

def submit():
    name = name_entry.get()
    phone = phone_entry.get()
    age = age_entry.get()
    sex = sex_var.get()  # Get the value from the dropdown
    email = email_entry.get()
    inquiry = inquiry_entry.get()
    
    if not all([name, phone, age, sex, email, inquiry]):
        messagebox.showerror("Error", "Please fill all fields")
        return
    
    wb = openpyxl.load_workbook('barber_shop_data.xlsx')
    ws = wb.active
    ws.append([name, phone, age, sex, email, inquiry])
    wb.save('barber_shop_data.xlsx')
    
    messagebox.showinfo("Success", "Inquiry submitted successfully!")
    clear_fields()

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    inquiry_entry.delete(0, tk.END)
    sex_var.set('')  # Clear dropdown

# Create Excel file if it doesn't exist
create_excel_if_not_exists()

# Set up the main window
root = tk.Tk()
root.title("Barber Shop Enquiry")
root.geometry("800x500")  # Adjusted the window height
root.resizable(False, False)

# Load and set custom font
custom_font = font.Font(family="Helvetica", size=10)
title_font = font.Font(family="Playfair", size=24, weight="bold")

# Load and set background image
bg_image = Image.open("bg.png")  # Replace with the correct file path for the barber shop image
bg_image = bg_image.resize((400, 500), Image.LANCZOS)  # Adjusted height
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, width=400, height=500)

# Create right side frame
right_frame = tk.Frame(root, bg="#2c2c2c")
right_frame.place(x=400, y=0, width=400, height=500)  # Adjusted height

# Title
title_label = tk.Label(right_frame, text="CONTACT US", font=title_font, bg="#2c2c2c", fg="#DCC494")  # Updated font color
title_label.pack(pady=(30, 20))  # Adjusted padding

# Create form fields
form_frame = tk.Frame(right_frame, bg="#2c2c2c")
form_frame.pack(fill="both", expand=True, padx=30)

labels = ["NAME", "Phone Number", "AGE", "SEX", "EMAIL ADDRESS", "INQUIRY"]
entries = []

for i, label_text in enumerate(labels):
    label = tk.Label(form_frame, text=label_text, font=custom_font, bg="#2c2c2c", fg="#DCC494", anchor="w")  # Updated font color
    if label_text == "AGE":
        label.grid(row=i*2, column=0, sticky="w", pady=(0, 5))
        entry = tk.Entry(form_frame, font=custom_font, bg="white", width=8, relief="solid", highlightbackground="#DCC494")  # Added rounded input fields
        entry.grid(row=i*2+1, column=0, sticky="w", pady=(0, 15))
        age_entry = entry
    elif label_text == "SEX":
        label.grid(row=(i-1)*2, column=1, sticky="w", padx=(10, 0), pady=(0, 5))  # Placed beside AGE
        sex_var = tk.StringVar()  # Variable to hold the dropdown value
        sex_menu = ttk.Combobox(form_frame, textvariable=sex_var, values=["Male", "Female", "Other"], font=custom_font, width=10)  # Slightly wider for better fit
        sex_menu.grid(row=i*2-1, column=1, sticky="w", padx=(10, 0), pady=(0, 15))
    else:
        label.grid(row=i*2, column=0, columnspan=2, sticky="w", pady=(0, 5))
        entry = tk.Entry(form_frame, font=custom_font, bg="white", width=30, relief="solid", highlightbackground="#DCC494")  # Added rounded input fields
        entry.grid(row=i*2+1, column=0, columnspan=2, sticky="ew", pady=(0, 15))
        if label_text == "NAME":
            name_entry = entry
        elif label_text == "Phone Number":
            phone_entry = entry
        elif label_text == "EMAIL ADDRESS":
            email_entry = entry
        elif label_text == "INQUIRY":
            inquiry_entry = entry

# Adjust layout for AGE and SEX fields
form_frame.grid_columnconfigure(0, weight=1)

# Create and place the submit button
submit_button = tk.Button(right_frame, text="Submit", command=submit, bg="#4CAF50", fg="white", font=custom_font, relief=tk.FLAT)
submit_button.pack(pady=30, ipadx=50, ipady=5)

root.mainloop()
