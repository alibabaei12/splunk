from tkinter import *
import tkinter as tk

import HomePage
import Files
import Folders
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
        self.folders_files = []

        self.currentPath = "home"

    def getCurrentPath(self):

        cmd_pwd = "pwd"

        stdin,stdout,stderr = self.hp.exec_command(cmd_pwd)

        stdout = stdout.readlines()

        print("the pwd comment returns: " + str(stdout))
        global currentLocation
        currentLocation = stdout[0]

        clean = str(stdout)
        clean = "Current Location is: " + clean[2:len(clean)-4]

        self.currentPath = clean

    def getFile_folders(self):

        stdin, stdout, stderr = self.hp.exec_command("ls -l")

        stdout = stdout.readlines()

        print("the pwd comment returns: " + str(stdout))
        st = None
        # see if its a file or folder and get the name as well
        for i in stdout:
            st = i.split(" ")
            name = st[len(st) - 1]
            if st[0][0] == 'd':
                folder = Folders.Folder(name, currentLocation)
                print("folder is " + folder.name)
                self.folders_files.append(folder)
            elif st[0][0] == '-':
                file = Files.File(name, "empty")
                print("file name is: " + file.name)
                self.folders_files.append(file)


        # print (st[len(st)-1])
        # print(st[0][0])

        # fs = self.controller.get_page("FileSystemWindow")
        # fs.text.set(clean)

    def func(self):
        self.getFile_folders()
        self.getCurrentPath()


        self.controller.framess([FileSystem.FileSystemWindow])

        self.controller.show_frame("FileSystemWindow", "File System Page")
