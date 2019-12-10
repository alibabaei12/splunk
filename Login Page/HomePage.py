from tkinter import *
from tkinter import messagebox
import tkinter as tk
import paramiko
import db.db

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

        self.cmdLabel = Label(self, text="Command:")
        self.cmdLabel.config(font=("Courier", 14, 'bold'))
        self.cmdLabel.place(x=60, y=250)

        self.command = Entry(self, font='Courier 12', width=40)
        self.command.place(x=150, y=250)

        # Making the Connect Button
        self.login_button = Button(self, text='Connect', font='Courier 15 bold', command=self.connectToServer)
        self.login_button.place(x=230, y=310)


    def connectToServer(self):
        pass
        # Connect to the server

        # host = 35.223.103.101
        # username= alibabaei12
        # password='Amirbaba12345'

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #ssh_client.connect(self.host_name.get(), username=self.username, password=self.password)
        ssh_client.connect(hostname="35.223.103.101", username="alibabaei12", password="Amirbaba12345")
        cmd = self.command.get()

        stdin,stdout,stderr = ssh_client.exec_command(cmd)

        stdout = stdout.readlines()

        print(stdout)
        # try:
        #     with pysftp.Connection(host=self.host_name.get(), username=self.username.get(), password=self.password.get(), cnopts=self.cnopts) as sftp:
        #         pass
        # except EXCEPTION as e:
        #     print(str(e))


