from tkinter import *
from tkinter import messagebox
import tkinter as tk
import paramiko


import HomePage
import ConnectPage
class FileSystemWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.hp = HomePage.ssh_client

        # Current Location
        print(ConnectPage.currentLocation)
        self.text = tk.StringVar()
        self.text.set("bla")
        self.cmdLabel = Label(self, textvariable= self.text)
        # self.cmdLabel.setvar()
        self.cmdLabel.config(font=("Courier", 14, 'bold'))
        self.cmdLabel.place(x=160, y=50)


        # Show Files
        

        #Buttons
        # Making the Connect Button
        self.execute_button = Button(self, text='View Files',width="13",height="2", font='Courier 18 bold', command=lambda: controller.show_frame("LogWindow", "Log Page"))
        self.execute_button.place(x=430, y=510)


    def getCurrentPath(self):

        cmd_pwd = "pwd"

        print(cmd_pwd)

        stdin,stdout,stderr = self.hp.exec_command(cmd_pwd)

        stdout = stdout.readlines()

        print(stdout)
        return stdout
        # self.myscroll = tk.Scrollbar(self, orient='vertical')
        # self.listbox = Listbox(self, yscrollcommand=self.myscroll.set, width=55, height=20)
        # for i in stdout:
        #     self.listbox.insert(END, i)
        # self.listbox.place(x=60, y=110)