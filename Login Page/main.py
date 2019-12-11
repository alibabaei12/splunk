import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from LoginPage import LoginWindow
from RegisterPage import RegisterWindow
from HomePage import HomeWindow
import ConnectPage
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.geometry("500x600+300+300")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, LoginWindow, RegisterWindow, HomeWindow, ConnectPage.ConnectWindow):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage", "Start Page")

    def show_frame(self, page_name, title):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        self.title(title)
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        # button1 = tk.Button(self, text="Login",
        #                     command=lambda: controller.show_frame("LoginWindow", "Login Page"))
        button1 = tk.Button(self, text="Home",
                            command=lambda: controller.show_frame("HomeWindow", "Home Page"))

        button2 = tk.Button(self, text="Register",
                            command=lambda: controller.show_frame("RegisterWindow", "Register Page"))
        button1.pack()
        button2.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()