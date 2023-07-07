from tkinter import *
import customtkinter

# Setting up theme for your app.
customtkinter.set_appearance_mode('dark')

# create CTK window
root = customtkinter.CTk()

# Setting window width and height
root.geometry('300x400')

# Create a button widget

# mybutton = Button(root, text='Hello World', font=("Inter", 14))
button = customtkinter.CTkButton(master=root, text="Hello World")

# Showing at the center of the screen
# mybutton.place(relx=0.5, rely=0.5, anchor=CENTER)
button.place(relx=0.5, rely=0.5, anchor=CENTER)

# Running the app
root.mainloop()
