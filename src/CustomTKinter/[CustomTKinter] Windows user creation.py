from tkinter import *
import customtkinter
import subprocess
import os

#Theme of Application
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
customtkinter.deactivate_automatic_dpi_awareness()

def create_account():

    end_username = username.get()
    end_password = password.get()
    is_checked =  admin_check.get()

    COMMAND = f"net user {end_username} {end_password} /add"
    if is_checked:
        COMMAND += " /add"

    subprocess.run(COMMAND, shell=True)    

root = customtkinter.CTk()

root.title('Offline Account Creator')
root.geometry('350x350')
root.iconbitmap(r'C:\Users\2380\OneDrive - FernUni Schweiz\Dokumente\GitHub\tKinter-experiment\src\CustomTKinter\Pictogrammers-Material-Account.512.ico')


title = customtkinter.CTkLabel(root, text="Account Creator", font=('Bold Calibri', 25))
title.place(relx=0.25, rely=0.1)

username = customtkinter.CTkEntry(root, corner_radius=10, width=140, height=40, fg_color="#ffffff", text_color="#000000", placeholder_text="Username")
username.place(relx=0.3, rely=0.3)

password = customtkinter.CTkEntry(root, corner_radius=10, width=140, height=40, fg_color="#ffffff", text_color="#000000", placeholder_text="Password")
password.configure(show="*")
password.place(relx=0.3, rely=0.45)

admin_check_var = BooleanVar()
admin_check = customtkinter.CTkCheckBox(root, corner_radius=10, fg_color="#ffffff", checkmark_color="#000000", text="Administrator", variable=admin_check_var)
admin_check.place(relx=0.35, rely=0.625)

def submit_pressed():
    create_account()

submit = customtkinter.CTkButton(root, corner_radius=10, text="Submit", fg_color="#ffffff", hover_color="#A9A9A9", text_color="#000000", command=submit_pressed)
submit.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)


root.mainloop()




  

