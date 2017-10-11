from tkinter import *

class gui(Frame):
    master = None
    def __init__(self):
        self.master = Tk()
        Frame.__init__(self, self.master)
        self.pack()
        self.guiBase()

    def guiBase(self):
        self.master.title("Lemonator Simulator")
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(500, 500))
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack()