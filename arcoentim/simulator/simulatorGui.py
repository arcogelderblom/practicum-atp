from tkinter import *

class Simulator(Frame):
    level = 0
    color = 10
    heater = 20
    sirupPumpValue = "Off"
    sirupValveValue = "Off"
    waterPumpValue = "Off"
    waterValveValue = "Off"

    def __init__(self, master=None):
        self.master = master
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def updateValues(self):
        print("hello")
        self.master.after(1000, self.updateValues())

    def createWidgets(self):
        ## Quit Button
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack()

        ## Label for level sensor
        self.levelSensor = Label(self.master, text="Level Sensor: {}".format(self.level))
        self.levelSensor.pack()

        ## Label for color sensor
        self.colorSensor = Label(self.master, text="Color Sensor: {}".format(self.color))
        self.colorSensor.pack()

        ## Label for heater
        self.heater = Label(self.master, text="Heater Temperature: {} celsius".format(self.heater))
        self.heater.pack()

        ## Label for sirup pump
        self.sirupPump = Label(self.master, text="Sirup Pump: {}".format(self.sirupPumpValue))
        self.sirupPump.pack()

        ## Label for sirup valve
        self.sirupValve = Label(self.master, text="Sirup Valve: {}".format(self.sirupValveValue))
        self.sirupValve.pack()

        ## Label for water pump
        self.waterPump = Label(self.master, text="Water Pump: {}".format(self.waterPumpValue))
        self.waterPump.pack()

        ## Label for water valve
        self.waterValve = Label(self.master, text="Water Valve: {}".format(self.waterValveValue))
        self.waterValve.pack()

    def updateLabels(self):
        pass


