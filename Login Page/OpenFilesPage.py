import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3

class OpenFiles(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.geometry("630x600+500+200")
        self.resizable(False,False)

