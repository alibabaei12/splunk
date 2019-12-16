from tkinter import *
from tkinter import messagebox
import tkinter as tk
import paramiko

import Files
import Folders
import HomePage
import ConnectPage
class FileSystemWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


        self.controller = controller
        self.parent = parent

        self.hp = HomePage.ssh_client

        self.connectPage = self.controller.get_page("ConnectWindow")
        # Current Location
        print("current path in file sys is: " + self.connectPage.currentPath)

        self.text = self.connectPage.currentPath

        self.cmdLabel = Label(self, text= self.connectPage.currentPath)
        # self.cmdLabel.setvar()
        self.cmdLabel.config(font=("Courier", 14, 'bold'))
        self.cmdLabel.place(x=160, y=50)


        # Show Files
        # Declare a list for folders and files in each path
        # self.folders = []
        # self.files = []

        self.x = 50
        self.y = 100


        # print(len(self???.connectPage.folders))
        self.folder_img = PhotoImage(file='img/folder_icon.png')
        self.adjust_folder_img = self.folder_img.subsample(3,3)

        self.file_img = PhotoImage(file='img/files.png')
        self.adjust_file_img = self.file_img.subsample(3,3)

        #print("filesystem folder name is: " + self.connectPage.folders[0].name)
        for i in self.connectPage.folders_files:
            if type(i) == Folders.Folder:
                self.folder_button = Button(self, width="80", height="70", image=self.adjust_folder_img)
            elif type(i) == Files.File:
                self.folder_button = Button(self, width="80", height="70", image=self.adjust_file_img)
            self.folder_button.place(x=self.x , y=self.y)
            self.folder_label = Label(self, text=i.name)
            self.folder_label.place(x=self.x, y = self.y +90)
            self.x = self.x + 150
            if self.x > 500 :
                self.x = 50
                self.y = self.y + 150
            else:
                continue




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