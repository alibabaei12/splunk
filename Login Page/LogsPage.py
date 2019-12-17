import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3

class LogsWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # button1 = tk.Button(self, text="Login",
        #                     command=lambda: controller.show_frame("LoginWindow", "Login Page"))

