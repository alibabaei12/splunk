from tkinter import *
from tkinter import messagebox
import tkinter as tk
import paramiko

import ConnectPage
import db.db

global ssh_client
ssh_client = paramiko.SSHClient()

class HomeWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Get the host name, username, and password to connect to the server
        self.label_host = tk.Label(self, text="Host:")
        self.label_host.config(font=("Courier", 14 , 'bold'))
        self.label_host.place(x=60,y=100)

        self.host_name = Entry(self, font='Courier 12', width=40)
        self.host_name.place(x=150, y=100)

        self.label_username = tk.Label(self, text="Username:")
        self.label_username.config(font=("Courier", 14, 'bold'))
        self.label_username.place(x=60, y=150)

        self.username = Entry(self, font='Courier 12', width=40)
        self.username.place(x=150, y=150)

        self.psLabel = Label(self, text="Password:")
        self.psLabel.config(font=("Courier", 14, 'bold'))
        self.psLabel.place(x=60, y=200)

        self.password = Entry(self, show="*", font='Courier 12', width=40)
        self.password.place(x=150, y=200)

        # Making the Connect Button
        self.connect_button = Button(self, text='Connect', font='Courier 15 bold', command=self.connectToServer)
        self.connect_button.place(x=230, y=410)


    def connectToServer(self):
        # Connect to the server
        # host = 35.223.103.101
        # username= alibabaei12
        # password='Amirbaba12345'
        self.controller.framess([ConnectPage.ConnectWindow])
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #ssh_client.connect(self.host_name.get(), username=self.username, password=self.password)
        try:
            ssh_client.connect(hostname="35.223.103.101", username="alibabaei12", password="Amirbaba12345")
            self.controller.show_frame("ConnectWindow", "Connect Page")
        except EXCEPTION as e:
            print(e)


