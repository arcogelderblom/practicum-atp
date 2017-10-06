from tkinter import *
import lemonatorLogger
from copy import deepcopy
#import lemonator

class Simulator(Frame):
    """
    ## HW variables with lemonator

    hw = lemonator.lemonator(2)
    waterLevel = hw.distance #The example shows this however i can not test it
    heater = hw.heather
    liquidTemperature = hw.temperature
    color = hw.color
    sirupPumpValue = hw.sirup_pump
    sirupValveValue = hw.sirup_valve
    waterPumpValue = hw.water_pump
    waterValveValue = hw.water_valve
    lcd = hw.lcd
    keypad = hw.keypad
    liquidTemperature = hw.temperature
    isCupPresent = hw.reflex
    greenLed = hw.led_green
    yellowLed = hw.led_yellow
    """

    ## HW variables without lemonator

    waterLevel = 0
    heater = 0
    liquidTemperature = 0
    color = 0
    sirupPumpValue = 0
    sirupValveValue = 0
    waterPumpValue = 0
    waterValveValue = 0
    lcd = 0
    keypad = 0
    liquidTemperature = 0
    isCupPresent = 0
    greenLed = 0
    yellowLed = 0

    ## Logger
    log = lemonatorLogger.lemonatorLogger("log.txt")

    def __init__(self, master=None):
        self.master = master
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def updateValues(self):
        print("hello")
        self.updateLabels()
        self.master.after(1000, self.updateValues)

    def keypadButton(self, buttonValue):
        print("Button pressed with value: ", buttonValue)

        ## Only a few have been added now the rest comes later when we know what to do with them
        correspondingActions = {1: lambda: print(1),
                                2: lambda: print(2),
                                3: lambda: print(3)}

        ## Execute watever the lambda function needs to
        correspondingActions[buttonValue]()

    def createWidgets(self):
        ## Quit Button
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack()

        ## Label for level sensor
        self.levelSensor = Label(self.master, text="Level Sensor: {}".format(self.waterLevel))
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

        ## Keypad
        self.waterValve = Label(self.master, text="Keypad buttons:")
        self.waterValve.pack()

        #self.b1 =
        #buttonList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '*', '#', 'A', 'B', 'C', 'D']
        #buttons = []
        #for i in range(0, len(buttonList)):
        #    buttons.append(Button(self.master, text=str(buttonList[i]), command=lambda: self.keypadButton(deepcopy(buttonList[i]))).pack())
        Button(self.master, text="1", command=lambda: self.keypadButton(1)).pack()
        Button(self.master, text="2", command=lambda: self.keypadButton(2)).pack()
        Button(self.master, text="3", command=lambda: self.keypadButton(3)).pack()
        Button(self.master, text="4", command=lambda: self.keypadButton(4)).pack()
        Button(self.master, text="5", command=lambda: self.keypadButton(5)).pack()
        Button(self.master, text="6", command=lambda: self.keypadButton(6)).pack()
        Button(self.master, text="7", command=lambda: self.keypadButton(7)).pack()
        Button(self.master, text="8", command=lambda: self.keypadButton(8)).pack()
        Button(self.master, text="9", command=lambda: self.keypadButton(9)).pack()
        Button(self.master, text="0", command=lambda: self.keypadButton(0)).pack()
        Button(self.master, text="*", command=lambda: self.keypadButton('*')).pack()
        Button(self.master, text="#", command=lambda: self.keypadButton('#')).pack()
        Button(self.master, text="A", command=lambda: self.keypadButton('A')).pack()
        Button(self.master, text="B", command=lambda: self.keypadButton('B')).pack()
        Button(self.master, text="C", command=lambda: self.keypadButton('C')).pack()
        Button(self.master, text="D", command=lambda: self.keypadButton('D')).pack()


    def updateLabels(self):
        pass
        """
        ## Update all variables
        self.waterLevel = self.hw.distance
        self.color = self.hw.color
        self.heater = self.hw.heather
        self.sirupPumpValue = self.hw.sirup_pump
        self.sirupValveValue = self.hw.sirup_valve
        self.waterPumpValue = self.hw.water_pump
        self.waterValveValue = self.hw.water_valve

        ## Update labels
        self.levelSensor.config(text="Level Sensor: {}".format(self.level))

        ## Log updated variables
        log.addSensorInfoLine("waterLevelSensor", self.waterLevel)
        log.addSensorInfoLine("color", self.color)
        log.addSensorInfoLine("heater", self.heater)
        log.addSensorInfoLine("sirupPumpValue", self.sirupPumpValue)
        log.addSensorInfoLine("sirupValveValue", self.sirupValveValue)
        log.addSensorInfoLine("waterPumpValue", self.waterPumpValue)
        log.addSensorInfoLine("waterValveValue", self.waterValveValue)
        """

