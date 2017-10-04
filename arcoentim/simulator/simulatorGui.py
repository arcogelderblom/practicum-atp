from tkinter import *
import lemonator

class Simulator(Frame):
    hw = lemonator.lemonator(2)
    level = hw.distance #The example shows this however i can not test it
    color = hw.color
    heater = hw.heather
    sirupPumpValue = hw.sirup_pump
    sirupValveValue = hw.sirup_valve
    waterPumpValue = hw.water_pump
    waterValveValue = hw.water_valve

    ## We might also be missing these values, but i am not sure if we are supposed to use them
    #lcd = hw.lcd
    #keypad = hw.keypad
    #liquidTemperature = hw.temperature
    #isCupPresent = hw.reflex
    #greenLed = hw.led_green
    #yellowLed = hw.led_yellow

    def __init__(self, master=None):
        self.master = master
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def updateValues(self):
        print("hello")
        self.updateLabels()
        self.master.after(1000, self.updateValues)

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
        ## Update all variables
        self.level = self.hw.distance
        self.color = self.hw.color
        self.heater = self.hw.heather
        self.sirupPumpValue = self.hw.sirup_pump
        self.sirupValveValue = self.hw.sirup_valve
        self.waterPumpValue = self.hw.water_pump
        self.waterValveValue = self.hw.water_valve

        ## Update labels
        self.levelSensor.config(text="Level Sensor: {}".format(self.level))


