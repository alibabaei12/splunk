from tkinter import *
from tkinter import messagebox
import tkinter as tk
import paramiko
import db.db
import HomePage
import main
class ConnectWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.cmdLabel = Label(self, text="Command:")
        self.cmdLabel.config(font=("Courier", 14, 'bold'))
        self.cmdLabel.place(x=60, y=250)

        self.command = Entry(self, font='Courier 12', width=40)
        self.command.place(x=150, y=250)

        # Making the Connect Button
        self.execute_button = Button(self, text='Execute', font='Courier 15 bold', command=self.connectToServer)
        self.execute_button.place(x=230, y=410)


    def connectToServer(self):

        self.hp = HomePage.ssh_client



        cmd = self.command.get()
        print(cmd)
        stdin,stdout,stderr = self.hp.exec_command(cmd)

        stdout = stdout.readlines()

        self.prt = Label(self,text = stdout)
        self.prt.config(font=("Courier", 14, 'bold'))
        self.prt.place(x=60, y=310)
        # try:
        #     with pysftp.Connection(host=self.host_name.get(), username=self.username.get(), password=self.password.get(), cnopts=self.cnopts) as sftp:
        #         pass
        # except EXCEPTION as e:
        #     print(str(e))


