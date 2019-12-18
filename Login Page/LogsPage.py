import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3

import Files
import Folders
import HomePage


class LogsWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # button1 = tk.Button(self, text="Login",
        #                     command=lambda: controller.show_frame("LoginWindow", "Login Page"))

        # self.hp = HomePage.ssh_client
        #
        # self.connectPage = self.controller.get_page("ConnectWindow")
        #
        # self.x = 50
        # self.y = 100
        #
        # # print(len(self???.connectPage.folders))
        # self.folder_img = tk.PhotoImage(file='img/folder_icon.png')
        # self.adjust_folder_img = self.folder_img.subsample(3, 3)
        #
        # self.file_img = tk.PhotoImage(file='img/files.png')
        # self.adjust_file_img = self.file_img.subsample(3, 3)
        #
        # self.back_img = tk.PhotoImage(file="img/back-button.png")
        # self.adjust_back_img = self.back_img.subsample(3, 3)
        #
        # self.back_button = tk.Button(self, width="60", height="50", image=self.adjust_back_img,
        #                           command=lambda: self.connectPage.cd(".."))
        # self.back_button.place(x=20, y=20)
        # # print("filesystem folder name is: " + self.connectPage.folders[0].name)
        # self.file_buttons = {}
        # self.folder_buttons = {}
        # for i in self.connectPage.log_files:
        #     if type(i) == Folders.Folder:
        #         self.folder_buttons[i] = tk.Button(self, width="80", height="70", image=self.adjust_folder_img,
        #                                         command=lambda i=i: self.connectPage.cd(i.name))
        #
        #
        #     elif type(i) == Files.File:
        #         self.folder_buttons[i] = tk.Button(self, width="80", height="70", image=self.adjust_file_img)
        #
        # for i in self.folder_buttons.keys():
        #
        #     self.folder_buttons[i].place(x=self.x, y=self.y)
        #     self.folder_label = tk.Label(self, text=i.name)
        #     self.folder_label.place(x=self.x, y=self.y + 90)
        #     self.x = self.x + 150
        #     if self.x > 500:
        #         self.x = 50
        #         self.y = self.y + 150
        #     else:
        #         continue