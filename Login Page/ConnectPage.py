from tkinter import *
import tkinter as tk

import HomePage

import FileSystem
currentLocation = "Ali"
class ConnectWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.hp = HomePage.ssh_client

        # Making the Connect Button
        self.execute_button = Button(self, text='File System',width="20",height="2", font='Courier 26 bold', command=self.func)
        self.execute_button.place(x=150, y=110)



    def getCurrentPath(self):

        cmd_pwd = "pwd"

        print(cmd_pwd)

        stdin,stdout,stderr = self.hp.exec_command(cmd_pwd)

        stdout = stdout.readlines()

        print(str(stdout))
        global currentLocation
        currentLocation = stdout

        clean = str(stdout)
        clean = "Current Location is: " + clean[2:len(clean)-4]

        fs = self.controller.get_page("FileSystemWindow")
        fs.text.set(clean)

    def func(self):
        self.getCurrentPath()
        self.controller.show_frame("FileSystemWindow", "File System Page")
