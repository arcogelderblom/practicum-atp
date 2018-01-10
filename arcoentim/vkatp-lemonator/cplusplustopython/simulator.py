import controller
import gui
import simulatorGui
from tkinter import *

class simulator():
    #hwInterface = None
    control = None
    sim = None

    gui = None#test variable

    def __init__(self, startController):
        self.startController = startController
        self.guiBase()

    def guiBase(self):
        ## Create gui
        self.gui = gui.gui()

        ## Add simulator gui items
        self.sim = simulatorGui.simulatorGui()

        ## Add controller items
        if self.startController:
            self.control = controller.controller()

        self.updateValues()
        self.gui.master.mainloop()
        try:
            self.gui.master.destroy()
        finally:
            print("App has been destroyed")

    def updateValues(self):
        self.sim.updateLabels()
        if self.startController:
            self.control.updateLabels()
        self.gui.master.after(100, self.updateValues)
