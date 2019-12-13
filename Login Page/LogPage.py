from tkinter import *
from tkinter import messagebox
import tkinter as tk
import paramiko
from pip._vendor.pyparsing import basestring

import db.db
import HomePage

class LogWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.cmdLabel = Label(self, text="Command:")
        self.cmdLabel.config(font=("Courier", 14, 'bold'))
        self.cmdLabel.place(x=60, y=50)

        self.command = Entry(self, font='Courier 12', width=40)
        self.command.place(x=150, y=50)

        # Making the Connect Button
        self.execute_button = Button(self, text='Execute', font='Courier 15 bold', command=self.connectToServer)
        self.execute_button.place(x=230, y=510)


    def connectToServer(self):

        self.hp = HomePage.ssh_client

        cmd = self.command.get()
        print(cmd)
        stdin,stdout,stderr = self.hp.exec_command(cmd)

        stdout = stdout.readlines()

        print(stdout)

        self.myscroll = tk.Scrollbar(self, orient='vertical')
        self.listbox = Listbox(self, yscrollcommand=self.myscroll.set, width=55, height=20)
        for i in stdout:
            self.listbox.insert(END, i)
        self.listbox.place(x=60, y=110)
