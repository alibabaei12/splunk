import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3

class OpenFiles(tk.Tk):

    def __init__(self, title,files, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.geometry("630x600+1000+200")
        self.resizable(False,False)
        self.title(title)

        myscroll = tk.Scrollbar(self, orient='vertical')
        listbox = tk.Listbox(self, yscrollcommand=myscroll.set, width=63, height=27)
        for i in files:
            listbox.insert(tk.END, i)
        listbox.place(x=30, y=100)