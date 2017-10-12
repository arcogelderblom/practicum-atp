from tkinter import *
import lemonatorLogger
import lemonator
import gui

class simulatorGui():
    userInterface = gui.gui
    hwInterface = gui.sharedVariables()
    log = lemonatorLogger.lemonatorLogger("log.txt")

    # Variables for amounts
    userLemonadeValue = "0"
    userWaterValue = "0"
    userSelectLemonade = True # True = lemonade, False = water
    userStartMixing = False

    def __init__(self, master=None):
        self.guiBase()

    def guiBase(self):
        ## Label for level sensor
        self.levelSensorLabel = Label(self.userInterface.master, text="Level Sensor: {} ml".format(self.hwInterface.read_mm("fluidLevel")))
        self.levelSensorLabel.pack()
        
        ## Label for heater
        #self.heaterLabel = Label(self.gui.master, text="Heater: {}".format(self.heater))
        #self.heaterLabel.pack()

        ## Label for liquid temperature
        self.liquidLabel = Label(self.userInterface.master, text="Liquid Temperature: {} celsius".format(self.hwInterface.read_mc("liquidTemperature")))
        self.liquidLabel.pack()

        ## Label for sirup pump
        #self.sirupPumpLabel = Label(self.gui.master, text="Sirup Pump: {}".format(self.sirupPumpValue))
        #self.sirupPumpLabel.pack()

        ## Label for sirup valve
        #self.sirupValveLabel = Label(self.gui.master, text="Sirup Valve: {}".format(self.sirupValveValue))
        #self.sirupValveLabel.pack()

        ## Label for water pump
        #self.waterPumpLabel = Label(self.gui.master, text="Water Pump: {}".format(self.waterPumpValue))
        #self.waterPumpLabel.pack()

        ## Label for water valve
        #self.waterValveLabel = Label(self.gui.master, text="Water Valve: {}".format(self.waterValveValue))
        #self.waterValveLabel.pack()

        ## Cup present label
        self.cupPresentLabel = Label(self.userInterface.master, text="Is a cup present: {}".format(self.hwInterface.read_mc("isCupPresent")))
        self.cupPresentLabel.pack()

        ## Green led
        #self.greenLedLabel = Label(self.gui.master, text="Is green led on: {}".format(self.greenLed))
        #self.greenLedLabel.pack()

        ## Yellow led
        #self.yellowLedLabel = Label(self.gui.master, text="Is yellow led on: {}".format(self.yellowLed))
        #self.yellowLedLabel.pack()

        ## LCD
        #self.lcdValueLabel = Label(self.gui.master, text="LCD Value: {}".format(self.lcd))
        #self.lcdValueLabel.place(x=100, y=200)

        Button(self.userInterface.master, text="1", command=lambda: self.keypadButton(1)).place(x=160, y=300)
        Button(self.userInterface.master, text="2", command=lambda: self.keypadButton(2)).place(x=210, y=300)
        Button(self.userInterface.master, text="3", command=lambda: self.keypadButton(3)).place(x=260, y=300)
        Button(self.userInterface.master, text="4", command=lambda: self.keypadButton(4)).place(x=160, y=330)
        Button(self.userInterface.master, text="5", command=lambda: self.keypadButton(5)).place(x=210, y=330)
        Button(self.userInterface.master, text="6", command=lambda: self.keypadButton(6)).place(x=260, y=330)
        Button(self.userInterface.master, text="7", command=lambda: self.keypadButton(7)).place(x=160, y=360)
        Button(self.userInterface.master, text="8", command=lambda: self.keypadButton(8)).place(x=210, y=360)
        Button(self.userInterface.master, text="9", command=lambda: self.keypadButton(9)).place(x=260, y=360)
        Button(self.userInterface.master, text="0", command=lambda: self.keypadButton(0)).place(x=210, y=390)
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
        """
        ## Change variables
        if self.iscupPresent == "No":
            self.sirupPumpValue = 0
            self.sirupValveValue = 1
            self.waterPumpValue = 0
            self.waterValveValue = 1
            self.lcd = "Plz put a cup in the machine"
            #self.hw.lcd.set("Plz put a cup in the machine")
            #self.lcd = self.hw.lcd
        elif self.iscupPresent == "Yes":
            if self.userStartMixing:
                self.lcd = "Pouring your drink\nSelected amounts Water: " + str(int(self.userWaterValue)) + " Lemonade: " + str(int(self.userLemonadeValue))
                self.waterLevel += 1
                if self.waterLevel < int(self.userLemonadeValue):
                    self.lcd += "\nNow pouring: lemonade"
                    self.sirupValveValue = 0
                    self.sirupPumpValue = 1
                    self.waterPumpValue = 0
                    self.waterValveValue = 1

                elif self.waterLevel >= int(self.userLemonadeValue) and self.waterLevel < int(self.userWaterValue)+int(self.userLemonadeValue):
                    self.sirupValveValue = 1
                    self.sirupPumpValue = 0
                    self.waterPumpValue = 1
                    self.waterValveValue = 0
                    self.lcd += "\nNow pouring: water"
                else:
                    self.lcd = "Drink has been poured"
                    self.sirupValveValue = 1
                    self.sirupPumpValue = 0
                    self.waterPumpValue = 0
                    self.waterValveValue = 1
                    self.userStartMixing = False
                    self.userWaterValue = "0"
                    self.userLemonadeValue = "0"
                    #changin weglaten

            elif not self.userStartMixing:
                self.lcd = "Waiting for start(C) or values(A, B)\nSelected amounts Water: " + str(int(self.userWaterValue)) + " Lemonade: " + str(int(self.userLemonadeValue))
                self.sirupPumpValue = 0
                self.sirupValveValue = 1
                self.waterPumpValue = 0
                self.waterValveValue = 1
                self.waterLevel = 0
                if self.userSelectLemonade:
                    self.lcd += "\nChanging lemonade now"
                else:
                    self.lcd += "\nChanging water now"

		"""
        ## Update labels
        self.levelSensorLabel.config(text="Level Sensor: {} ml".format(self.hwInterface.read_mm("fluidLevel")))
        self.liquidLabel.config(text="Liquid Temperature: {} celsius".format(self.hwInterface.read_mc("liquidTemperature")))
        #self.heaterLabel.config(text="Heater: {}".format(self.heater))
        #self.sirupPumpLabel.config(text="Sirup Pump: {}".format(self.sirupPumpValue))
        #self.sirupValveLabel.config(text="Sirup Valve: {}".format(self.sirupValveValue))
        #self.waterPumpLabel.config(text="Water Pump: {}".format(self.waterPumpValue))
        #self.waterValveLabel.config(text="Water Valve: {}".format(self.waterValveValue))
        self.cupPresentLabel.config(text="Is a cup present: {}".format(self.hwInterface.get("isCupPresent")))
        #self.greenLedLabel.config(text="Is green led on: {}".format(self.greenLed))
        #self.yellowLedLabel.config(text="Is yellow led on: {}".format(self.yellowLed))
        #self.lcdValueLabel.config(text="LCD Value: {}".format(self.lcd))
        """
        ## Log updated variables
        self.log.addSensorInfoLine("waterlevelSensorLabel", self.waterLevel)
        self.log.addSensorInfoLine("Liquid temperature", self.liquidTemperature)
        self.log.addSensorInfoLine("heater", self.heater)
        self.log.addSensorInfoLine("sirupPumpLabelValue", self.sirupPumpValue)
        self.log.addSensorInfoLine("sirupValveLabelValue", self.sirupValveValue)
        self.log.addSensorInfoLine("waterPumpLabelValue", self.waterPumpValue)
        self.log.addSensorInfoLine("waterValveLabelValue", self.waterValveValue)
        self.log.addSensorInfoLine("is cup present", self.iscupPresent)
        self.log.addSensorInfoLine("green led on", self.greenLed)
        self.log.addSensorInfoLine("yellow led on", self.yellowLed)
        self.log.addSensorInfoLine("lcd", self.lcd)"""
