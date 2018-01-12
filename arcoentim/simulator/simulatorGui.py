from tkinter import *
import lemonatorLogger
import gui
from time import time

class simulatorGui():
    userInterface = gui.gui
    hwInterface = gui.sharedVariables()
    log = lemonatorLogger.lemonatorLogger("log.txt")

    def __init__(self):
        self.previousTime = time()
        self.guiBase()

    def guiBase(self):
        ## Label for level sensor
        self.levelSensorLabel = Label(self.userInterface.master, text="Level Sensor: {} ml".format(self.hwInterface.read_ml()))
        self.levelSensorLabel.pack()

        ## Label for sirup pump
        self.sirupPumpLabel = Label(self.userInterface.master, text="Sirup Pump: {}".format(self.hwInterface.get("sirupPump")))
        self.sirupPumpLabel.pack()

        ## Label for sirup valve
        self.sirupValveLabel = Label(self.userInterface.master, text="Sirup Valve: {}".format(self.hwInterface.get("sirupValve")))
        self.sirupValveLabel.pack()

        ## Label for water pump
        self.waterPumpLabel = Label(self.userInterface.master, text="Water Pump: {}".format(self.hwInterface.get("waterPump")))
        self.waterPumpLabel.pack()

        ## Label for water valve
        self.waterValveLabel = Label(self.userInterface.master, text="Water Valve: {}".format(self.hwInterface.get("waterValve")))
        self.waterValveLabel.pack()

        ## Cup present label
        self.cupPresentLabel = Label(self.userInterface.master, text="Is a cup present: {}".format(self.hwInterface.get("isCupPresent")))
        self.cupPresentLabel.pack()

        ## LCD
        self.lcdValueLabel = Label(self.userInterface.master, text="LCD Value: {}".format(self.hwInterface.getString()))
        self.lcdValueLabel.place(x=100, y=200)

        #Button(self.userInterface.master, text="Empty cup", command=lambda: self.hwInterface.write_mm(self.originalDistance)).place(x=330, y=180)
        Button(self.userInterface.master, text="Remove cup", command=lambda: self.hwInterface.set("isCupPresent", False)).place(x=330, y=210)
        Button(self.userInterface.master, text="Put cup in machine", command=lambda: self.hwInterface.set("isCupPresent", True)).place(x=330, y=240)


        Button(self.userInterface.master, text="1", command=lambda: self.keypadButton("1")).place(x=160, y=300)
        Button(self.userInterface.master, text="2", command=lambda: self.keypadButton("2")).place(x=210, y=300)
        Button(self.userInterface.master, text="3", command=lambda: self.keypadButton("3")).place(x=260, y=300)
        Button(self.userInterface.master, text="4", command=lambda: self.keypadButton("4")).place(x=160, y=330)
        Button(self.userInterface.master, text="5", command=lambda: self.keypadButton("5")).place(x=210, y=330)
        Button(self.userInterface.master, text="6", command=lambda: self.keypadButton("6")).place(x=260, y=330)
        Button(self.userInterface.master, text="7", command=lambda: self.keypadButton("7")).place(x=160, y=360)
        Button(self.userInterface.master, text="8", command=lambda: self.keypadButton("8")).place(x=210, y=360)
        Button(self.userInterface.master, text="9", command=lambda: self.keypadButton("9")).place(x=260, y=360)
        Button(self.userInterface.master, text="0", command=lambda: self.keypadButton("0")).place(x=210, y=390)
        Button(self.userInterface.master, text="*", command=lambda: self.keypadButton('*')).place(x=160, y=390)
        Button(self.userInterface.master, text="#", command=lambda: self.keypadButton('#')).place(x=260, y=390)
        Button(self.userInterface.master, text="A", command=lambda: self.keypadButton('A')).place(x=310, y=300)
        Button(self.userInterface.master, text="B", command=lambda: self.keypadButton('B')).place(x=310, y=330)
        Button(self.userInterface.master, text="C", command=lambda: self.keypadButton('C')).place(x=310, y=360)
        Button(self.userInterface.master, text="D", command=lambda: self.keypadButton('D')).place(x=310, y=390)

    def keypadButton(self, buttonValue):
        self.hwInterface.putCKeypad(buttonValue)

    def assignDrinkValues(self, value):
        if self.userSelectLemonade:
            self.userLemonadeValue += value
        else:
            self.userWaterValue += value


    def updateLabels(self):
        currentAmount = self.hwInterface.read_ml()
        cupPresent = self.hwInterface.get("isCupPresent")
        if not self.hwInterface.usingHardware:
            sirupPump = self.hwInterface.get("sirupPump")
            sirupValve = self.hwInterface.get("sirupValve")
            waterPump = self.hwInterface.get("waterPump")
            waterValve = self.hwInterface.get("waterValve")
        ## If the cup is not present reset the fluid level to 0
        if not cupPresent:
            self.hwInterface.write_ml(0)

        if not self.hwInterface.usingHardware:
            ## If the pumps are open add something to the mm value (should become substract)
            if sirupPump:
                currentTime = time()
                ## Wait for the 3 second rampup
                if currentTime - self.previousTime >= 3:
                    self.hwInterface.write_ml(currentAmount + 0.1)

            elif waterPump:
                # Set the previous time after switching pumps
                if not self.previousSet:
                    self.previousTime = time()
                    self.previousSet = True
                currentTime = time()
                ## Wait for the 3 second rampup
                if currentTime - self.previousTime >= 3:
                    self.hwInterface.write_ml(currentAmount + 0.1)

            else:
                self.previousTime = time()
                self.previousSet = False

            ## Update labels
            self.levelSensorLabel.config(text="Level Sensor: {} ml".format(currentAmount))
            self.sirupPumpLabel.config(text="Sirup Pump: {}".format(sirupPump))
            self.sirupValveLabel.config(text="Sirup Valve: {}".format(sirupValve))
            self.waterPumpLabel.config(text="Water Pump: {}".format(waterPump))
            self.waterValveLabel.config(text="Water Valve: {}".format(waterValve))

            ## Log updated variables
            self.log.addSensorInfoLine("waterlevelSensor", currentAmount)
            self.log.addSensorInfoLine("sirupPumpValue", sirupPump)
            self.log.addSensorInfoLine("sirupValveValue", sirupValve)
            self.log.addSensorInfoLine("waterPumpValue", waterPump)
            self.log.addSensorInfoLine("WaterValveValue", waterValve)

        self.cupPresentLabel.config(text="Is a cup present: {}".format(cupPresent))
        self.lcdValueLabel.config(text="LCD Value: {}".format(self.hwInterface.getString()))

        self.log.addSensorInfoLine("Reflex", cupPresent)
        self.log.addSensorInfoLine("lcd", self.hwInterface.getString())
