from tkinter import *
import tkinter as tk

import HomePage
import Files
import Folders
import FileSystem
import LogsPage
import OpenFilesPage

currentLocation = "Ali"

class ConnectWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        self.hp = self.controller.get_page("HomeWindow").hp

        # Making the Connect Button
        self.filesys_button = Button(self, text='File System',width="20",height="2", font='Courier 26 bold', command=self.func)
        self.filesys_button.place(x=150, y=110)

        self.controller.framess([LogsPage.LogsWindow])

        self.log_button = Button(self, text='Logs',width="20",height="2", font='Courier 26 bold', command=lambda: self.openLogsPage())
        self.log_button.place(x=150, y=200)
        self.folders_files = []
        self.log_files = []
        self.currentPath = "home"
        self.path = "blaaaa"

        self.init_path = "aaaaaa"
    def getCurrentPath(self):

        cmd_pwd = "pwd"

        stdin,stdout,stderr = self.hp.exec_command(cmd_pwd)

        stdout = stdout.readlines()

        # print("the pwd comment returns: " + str(stdout))
        global currentLocation
        currentLocation = stdout[0]

        clean = str(stdout)
        self.path = clean[2:len(clean)-4]
        self.init_path = self.path
        # print("initial path: " + self.path)
        clean = "Current Location is: " + clean[2:len(clean)-4]

        self.currentPath = clean

    def getFile_folders(self):

        stdin, stdout, stderr = self.hp.exec_command("ls -l")

        stdout = stdout.readlines()

        # print("the pwd comment returns: " + str(stdout))
        st = None
        # see if its a file or folder and get the name as well
        for i in stdout:
            st = i.split(" ")
            name = st[len(st) - 1]
            name = name[0: len(name)-1]
            # print("the name isssss: " + name)
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

        self.controller.framess([FileSystem.FileSystemWindow])

        self.controller.show_frame("FileSystemWindow", "File System Page")

    def cd(self, folder_name):

        self.folders_files.clear()
        # print("folder name is " + folder_name + " yayaya ")
        if self.path[len(self.path)-1] == "/":
            self.path = self.path[0: len(self.path)-1]



        if self.path == "" or self.path == "//":
            self.path = "/"

        # print("cd current path is: " + self.path)
        #if you want to go to the previous direcory
        if folder_name == ".." :
            # print("the pathhhhhhhhhh is : " + self.path)
            parse = self.path.split("/")
            self.path = ""
            # print("cd right before parsing current path is: " + self.path + "/.. ; ls -l")
            if parse[len(parse) - 1][len(parse[len(parse) - 1]) - 1:len(parse[len(parse) - 1])] == "\n":
                #remove the new line at the end of the parse
                parse[len(parse)-1] = parse[len(parse)-1][0:len(parse[len(parse)-1])-1]

            # print("the parse is: ", parse)
            for j in parse[0: len(parse)]:
                self.path += j + "/"

            # self.path = self.path[0: len(self.path) - 1]


            # self.path = self.path[0:len(self.path)-1]
            # print("The Path after parsing : " + self.path )
            command = "cd " + self.path + ".. ; ls -l"

            # print("command is: " + command)
            stdin, stdout, stderr = self.hp.exec_command(command)

            stderr = stderr.readlines()
            # print("the error is: " , stderr)
            back_path = self.path.split("/")
            # print("the back path is: " , back_path)
            self.path = ""
            #getting rid of the new line
            for k in back_path[0: len(parse)-1]:
                self.path += k + "/"

            # print("the path at the end is: " + self.path)

        else:


            if len(self.path) > 1 and self.path[len(self.path)-1] == "/":

                self.path += folder_name
                self.path = self.path[0:len(self.path) - 1]
            else:


                self.path += ("/" + folder_name)
                parse = self.path.split("/")
                # print("parse is: " , parse)

                self.path = ""
                # print("cd right before parsing current path is: " + self.path + "/.. ; ls -l")

                # remove the new line at the end of the parse

                # print("now parse is: ", parse)

                # print("the last letter is : " , parse[len(parse)-1][len(parse[len(parse)-1])-1:len(parse[len(parse)-1])])
                if parse[len(parse)-1][len(parse[len(parse)-1])-1:len(parse[len(parse)-1])] == "\n":
                    parse[len(parse) - 1] = parse[len(parse) - 1][0:len(parse[len(parse) - 1]) - 1]
                for j in parse[0: len(parse)]:
                    self.path += j + "/"

                self.path = self.path[0:len(self.path) - 1]

            # print("the cd path is; " + self.path + " ; ls -l")
            stdin, stdout, stderr = self.hp.exec_command("cd " + self.path + " ; ls -l")

        self.currentPath = "Current directory is: " + self.path

        stdout= stdout.readlines()


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

    def openFiles(self, file_name):

        cmd = "cat " + file_name

        stdin, stdout, stderr = self.hp.exec_command(cmd)

        stdout = stdout.readlines()


        app = OpenFilesPage.OpenFiles()
        app.mainloop()


        # clean = str(stdout)
        # self.path = clean[2:len(clean) - 4]
        # clean = "Current Location is: " + clean[2:len(clean) - 4]
        #
        # self.currentPath = clean

    def openLogsPage(self):
        self.controller.framess([LogsPage.LogsWindow])
        self.controller.show_frame("LogsWindow", "Logs Window")

    def show_files(self, file_name):

        parse = self.currentPath.split("/")
        folder_name= parse[len(parse)-1]
        print("parse is, " , parse)
        print("current path is: " + self.path)
        print("file name is: " + file_name)

        cmd = "cat " + self.path + "/" +file_name
        if folder_name == "log":
            cmd = "sudo " +  cmd
            cmd = cmd[0:len(cmd) - 1]
        else:
            pass


        print("last letter of cmd: " , cmd[len(cmd)-1])

        print("cmd is: " + cmd + " =======> see if it goes next line")

        stdin, stdout, stderr = self.hp.exec_command(cmd)
        stdout = stdout.readlines()

        print("the stdout is: ", stdout)
        print("the stderr is: ", stderr)

        return stdout


