from tkinter import *
from tkinter import messagebox
import tkinter as tk
import paramiko

import Files
import Folders
import HomePage
import ConnectPage
import LogPage
import OpenFilesPage


class ScrollFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent) # create a frame (self)

        self.canvas = tk.Canvas(self, width=562, height=392, borderwidth=0)          #place canvas on self
        self.viewPort = tk.Frame(self.canvas, width=562, height=200)                    #place a frame on the canvas, this frame will hold the child widgets
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview) #place a scrollbar on self
        self.canvas.configure(yscrollcommand=self.vsb.set)                          #attach scrollbar action to scroll of canvas

        self.vsb.pack(side="right", fill="y")                                       #pack scrollbar to right of self
        self.canvas.pack(side="left", fill="both", expand=True)                     #pack canvas to left of self and expand to fil
        self.canvas_window = self.canvas.create_window((4,4), window=self.viewPort, anchor="nw",            #add view port frame to canvas
                                  tags="self.viewPort")

        self.viewPort.bind("<Configure>", self.onFrameConfigure)                       #bind an event whenever the size of the viewPort frame changes.
        self.canvas.bind("<Configure>", self.onCanvasConfigure)                       #bind an event whenever the size of the viewPort frame changes.

        self.onFrameConfigure(None)                                                 #perform an initial stretch on render, otherwise the scroll region has a tiny border until the first resize

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))                 #whenever the size of the frame changes, alter the scroll region respectively.

    def onCanvasConfigure(self, event):
        '''Reset the canvas window to encompass inner frame when required'''
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_window, width = canvas_width)

class FileSystemWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent


        self.hp = self.controller.get_page("HomeWindow").hp

        self.connectPage = self.controller.get_page("ConnectWindow")
        # print("current path in file sys is: " + self.connectPage.currentPath)



        self.scrollFrame = ScrollFrame(self)  # add a new scrollable frame.





        self.text = self.connectPage.currentPath

        self.cmdLabel = Label(self, text= self.connectPage.currentPath)
        # self.cmdLabel.setvar()
        self.cmdLabel.config(font=("Courier", 14, 'bold'))
        self.cmdLabel.place(x=160, y=50)

        # Show Files
        # Declare a list for folders and files in each path
        # self.folders = []
        # self.files = []

        self.x = 20
        self.y = 20

        # print(len(self???.connectPage.folders))
        self.folder_img = PhotoImage(file='img/folder_icon.png')
        self.adjust_folder_img = self.folder_img.subsample(3,3)

        self.file_img = PhotoImage(file='img/files.png')
        self.adjust_file_img = self.file_img.subsample(3,3)

        self.back_img = PhotoImage(file="img/back-button.png")
        self.adjust_back_img = self.back_img.subsample(3,3)

        self.back_button = Button(self, width="60", height="50", image=self.adjust_back_img, command=lambda : self.connectPage.cd(".."))
        self.back_button.place(x= 20, y = 20)
        #print("filesystem folder name is: " + self.connectPage.folders[0].name)
        self.file_buttons = {}
        self.folder_buttons = {}
        for i in self.connectPage.folders_files:
            if type(i) == Folders.Folder:
                self.folder_buttons[i] = tk.Button(self.scrollFrame.viewPort, width="80", height="70", image=self.adjust_folder_img, command=lambda i = i: self.connectPage.cd(i.name))


            elif type(i) == Files.File:
                self.folder_buttons[i] = tk.Button(self.scrollFrame.viewPort, width="80", height="70", image=self.adjust_file_img, command= lambda i=i: self.file_clicked(i.name))

        self.myscroll = tk.Scrollbar(self, orient='vertical')

        self.r= 0
        self.c = 0
        for i in self.folder_buttons.keys():

            self.folder_buttons[i].grid(row=self.r, column=self.c,padx=10, pady=10)
            self.folder_label = Label(self.scrollFrame.viewPort, text= i.name)
            self.folder_label.grid(row=self.r+1, column=self.c)

            self.c = self.c + 1
            # print("row is: " , self.r)
            if self.c > 4:
                self.r = self.r + 2
                self.c = 0
            else:
                continue

        self.scrollFrame.place(x=20, y=88)
        # self.myscrollbar.place(x=500, y=100)
        # self.myscrollbar.config(command=self.canvas.yview)


        # self.canvas.place(x=0, y=0)

        #Buttons
        # Making the Connect Button
        self.controller.framess([LogPage.LogWindow])
        self.execute_button = Button(self, text='View Files',width="13",height="2", font='Courier 18 bold', command=lambda: controller.show_frame("LogWindow", "Log Page"))
        self.execute_button.place(x=430, y=510)


    def getCurrentPath(self):

        cmd_pwd = "pwd"

        # print(cmd_pwd)

        stdin,stdout,stderr = self.hp.exec_command(cmd_pwd)

        stdout = stdout.readlines()

        # print(stdout)
        return stdout
        # self.myscroll = tk.Scrollbar(self, orient='vertical')
        # self.listbox = Listbox(self, yscrollcommand=self.myscroll.set, width=55, height=20)
        # for i in stdout:
        #     self.listbox.insert(END, i)
        # self.listbox.place(x=60, y=110)

    def file_clicked(self, file_name):

        files = self.connectPage.show_files(file_name)
        title = file_name + " Window"
        of = OpenFilesPage.OpenFiles(title, files)

        # root = Tk()
        # root.geometry("630x600+1000+200")

        # root.title(title)

        #
        # root.mainloop()
        #
        # # make canvas to make the page scrollable
        # self.canvas = Canvas(self, width=562, height=392, scrollregion=(0, 0, 2000, 2000))
        #
        # # relief=GROOVE, width=570, height=400, bd=1
        # self.myframe = Frame(self.canvas, bg="blue")
        #
        # self.myscrollbar = Scrollbar(self, orient=VERTICAL, command=self.canvas.yview)
        #
        # self.canvas.configure(yscrollcommand=self.myscrollbar.set)
        #
        # self.myscrollbar.pack(side="right", fill="y")  # pack scrollbar to right of self
        # self.canvas.pack(side="left", fill="both", expand=True)
        # # self.myframe.place(x=20, y=88)
        #
        # self.canvas_window = self.canvas.create_window((4, 4), window=self.myframe, anchor="nw",
        #                                                # add view port frame to canvas
        #                                                tags="self.myframe")
        #
        # self.myframe.bind("<Configure>",
        #                   self.onFrameConfigure)  # bind an event whenever the size of the viewPort frame changes.
        # self.canvas.bind("<Configure>", self.onCanvasConfigure)
        #
        # self.onFrameConfigure(None)