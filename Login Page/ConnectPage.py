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
        self.path = "blaaaa"
    def getCurrentPath(self):

        cmd_pwd = "pwd"

        stdin,stdout,stderr = self.hp.exec_command(cmd_pwd)

        stdout = stdout.readlines()

        print("the pwd comment returns: " + str(stdout))
        global currentLocation
        currentLocation = stdout[0]

        clean = str(stdout)
        self.path = clean[2:len(clean)-4]
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
            name = name[0: len(name)-1]
            print("the name isssss: " + name)
            if st[0][0] == 'd':
                folder = Folders.Folder(name, currentLocation)

                self.folders_files.append(folder)
            elif st[0][0] == '-':
                file = Files.File(name, "empty")

                self.folders_files.append(file)


        # print (st[len(st)-1])
        # print(st[0][0])

        # fs = self.controller.get_page("FileSystemWindow")
        # fs.text.set(clean)

    def func(self):
        self.getFile_folders()
        self.getCurrentPath()

        print("fuc was called again")

        self.controller.framess([FileSystem.FileSystemWindow])

        self.controller.show_frame("FileSystemWindow", "File System Page")

    def cd(self, folder_name):

        self.folders_files.clear()
        # print("folder name is " + folder_name + " yayaya ")
        # print("cd current path is: " + self.path)

        #if you want to go to the previous direcory
        if folder_name == "..":
            parse = self.path.split("/")
            self.path = ""
            # print("cd right before parsing current path is: " + self.path + "/.. ; ls -l")

            parse[len(parse)-1] = parse[len(parse)-1][0:len(parse[len(parse)-1])-1]

            print("the parse is: ", parse)
            for j in parse[0: len(parse)]:
                self.path += j + "/"
            # self.path = self.path[0: len(self.path) - 1]


            # print("The Path after parsing : " + self.path[0:len(self.path)-1] + "/.. ; ls -l")
            self.path = self.path[0:len(self.path)-1]

            command = "cd " + self.path + "/.. ; ls -l"

            stdin, stdout, stderr = self.hp.exec_command(command)
            # print("command is: " + command)

            back_path = self.path.split("/")
            # print("the back path is: " , back_path)
            self.path = ""
            #getting rid of the new line
            for k in back_path[0: len(parse)-1]:
                self.path += k + "/"

            # print("the path at the end is: " + self.path)

        else:
            if self.path[len(self.path)-1] == "/":

                self.path += folder_name
                self.path = self.path[0:len(self.path) - 1]
            else:

                self.path += ("/" + folder_name)


            # print("the cd path is; " + self.path + " ; ls -l")
            stdin, stdout, stderr = self.hp.exec_command("cd " + self.path + " ; ls -l")



        self.currentPath = "Current directory is: " + self.path

        stdout= stdout.readlines()

        stderr = stderr.readlines()
        # print("tttttttttt " + str(stdout))
        # print ( "the error is: " + str(stderr) )

        for i in stdout:
            st = i.split(" ")
            name = st[len(st) - 1]
            if st[0][0] == 'd':
                folder = Folders.Folder(name, currentLocation)

                self.folders_files.append(folder)
            elif st[0][0] == '-':
                file = Files.File(name, "empty")

                self.folders_files.append(file)

        # print("currrr is : " + self.currentPath)
        # stdin, stdout, stderr = self.hp.exec_command("pwd")
        # stdout = stdout.readlines()
        # print("worrkkkk " + str(stdout))

        self.controller.framess([FileSystem.FileSystemWindow])
        self.controller.show_frame("FileSystemWindow", "File System Page")
