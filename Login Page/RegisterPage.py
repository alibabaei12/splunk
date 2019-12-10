from tkinter import *
from tkinter import messagebox
import tkinter as tk

import db.db

class RegisterWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller


        self.img = tk.PhotoImage(file='img/login-icon.png')

        self.label = tk.Label(self, image = self.img)
        self.label.pack(side="top", fill="x", pady=10)

        #Creating register Form


        self.label = tk.Label(self, text="User Login")
        self.label.config(font=("Courier", 20 , 'bold'))
        self.label.place(x=185,y=200)

        # Creating the email password labels

        self.name_label = tk.Label(self, text="Full Name")
        self.name_label.config(font=("Courier", 14 , 'bold'))
        self.name_label.place(x=20, y=260)

        self.name = Entry(self, font='Courier 12', width=40)
        self.name.place(x=150, y=260)

        self.emLabel = Label(self, text="Enter Email")
        self.emLabel.config(font=("Courier", 14, 'bold'))
        self.emLabel.place(x=20,y=290)

        self.email = Entry(self, font='Courier 12', width = 40)
        self.email.place(x=150, y=290)

        self.psLabel = Label(self, text="Enter Password")
        self.psLabel.config(font=("Courier", 14, 'bold'))
        self.psLabel.place(x=20, y= 320)

        self.password = Entry(self, show="*", font='Courier 12', width=40)
        self.password.place(x=150, y= 320)

        # Making the Register Buttons
        self.registerButton = Button(self, text='Register', font='Courier 15 bold', command=self.register)
        self.registerButton.place(x=230, y = 360)


        self.button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage", "Start Page"))
        self.button.place(x=200, y = 440)

    def register(self):
        # Get the data and store it into tuple (data)
        data = (
            self.name.get(),
            self.email.get(),
            self.password.get()
        )

        # Validation
        if self.email.get() == "":
            messagebox.showinfo("Alert!", "Enter Email First")
        elif self.password.get() == "":
            messagebox.showinfo("Alert!", "Enter Password")
        else:
            res = db.db.user_register(data)
            print(res)
            if res == 1:
                messagebox.showinfo("Message", "Register Successfully")
                self.controller.show_frame("StartPage", "Start Page")
            else:
                messagebox.showinfo("Alert!", "couldn't register")
