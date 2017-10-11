from tkinter import *
import lemonatorLogger
import lemonator
import gui

class rgbColor():
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    def __str__(self):
        return '(' + str(self.r) + ','+ str(self.r) + ',' + str(self.r) + ')'

class simulatorGui():
    ## HW variables with lemonator

    #get() is for bool
    #getc() is for keypad char
    #read_mm() is for distances
    #read_mc() is for reading sensor values as int
    #read_rgb() is for color sensor
    #set() is for setting variable

    hw = lemonator.lemonator( 4 )
    waterLevel = hw.distance.read_mm()
    heater = hw.heater
    liquidTemperature = hw.temperature
    color = hw.color
    sirupPumpValue = hw.sirup_pump
    sirupValveValue = hw.sirup_valve
    waterPumpValue = hw.water_pump
    waterValveValue = hw.water_valve
    #lcd = ""#hw.lcd
    #keypad = ""#hw.keypad
    iscupPresent = "No"#hw.reflex
    greenLed = hw.led_green
    yellowLed = hw.led_yellow

    #"""
    ## simulator variables
    #waterLevel = 0
    #liquidTemperature = 0
    #heater = "Off"
    #color = rgbColor(0, 0, 0)
    #sirupPumpValue = 0
    #sirupValveValue = 0
    #waterPumpValue = 0
    #waterValveValue = 0
    #iscupPresent = "No"
    #greenLed = "No"
    #yellowLed = "No"
    lcd = "Plz put cup in machine\nand specify an amount (A and B keys)"
    #"""

    # Variables for amounts
    userLemonadeValue = "0"
    userWaterValue = "0"
    userSelectLemonade = True # True = lemonade, False = water
    userStartMixing = False

    ## Logger
    log = lemonatorLogger.lemonatorLogger("log.txt")
    gui = gui.gui

    def __init__(self, master=None):
        self.guiBase()

    def guiBase(self):
        ## Label for level sensor
        self.levelSensorLabel = Label(self.gui.master, text="Level Sensor: {} ml".format(self.waterLevel))
        self.levelSensorLabel.pack()

        ## Label for heather
        self.heaterLabel = Label(self.gui.master, text="Heater: {}".format(self.heater))
        self.heaterLabel.pack()

        ## Label for liquid temperature
        self.liquidLabel = Label(self.gui.master, text="Liquid Temperature: {} celsius".format(self.liquidTemperature))
        self.liquidLabel.pack()

        ## Label for color sensor
        self.colorSensorLabel = Label(self.gui.master, text="Color Sensor: {}".format(self.color))
        self.colorSensorLabel.pack()

        ## Label for sirup pump
        self.sirupPumpLabel = Label(self.gui.master, text="Sirup Pump: {}".format(self.sirupPumpValue))
        self.sirupPumpLabel.pack()

        ## Label for sirup valve
        self.sirupValveLabel = Label(self.gui.master, text="Sirup Valve: {}".format(self.sirupValveValue))
        self.sirupValveLabel.pack()

        ## Label for water pump
        self.waterPumpLabel = Label(self.gui.master, text="Water Pump: {}".format(self.waterPumpValue))
        self.waterPumpLabel.pack()

        ## Label for water valve
        self.waterValveLabel = Label(self.gui.master, text="Water Valve: {}".format(self.waterValveValue))
        self.waterValveLabel.pack()

        ## Cup present label
        self.cupPresentLabel = Label(self.gui.master, text="Is a cup present: {}".format(self.iscupPresent))
        self.cupPresentLabel.pack()

        ## Green led
        self.greenLedLabel = Label(self.gui.master, text="Is green led on: {}".format(self.greenLed))
        # self.greenLedLabel.pack()

        ## Yellow led
        self.yellowLedLabel = Label(self.gui.master, text="Is yellow led on: {}".format(self.yellowLed))
        # self.yellowLedLabel.pack()

        ## LCD
        self.lcdValueLabel = Label(self.gui.master, text="LCD Value: {}".format(self.lcd))
        self.lcdValueLabel.place(x=100, y=200)

    #def assignDrinkValues(self, value):
    #    if self.userSelectLemonade:
    #        self.userLemonadeValue += value
    #    else:
    #        self.userWaterValue += value


    def updateLabels(self):
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


        ## Update labels
        self.levelSensorLabel.config(text="Level Sensor: {} ml".format(self.waterLevel))
        self.liquidLabel.config(text="Liquid Temperature: {} celsius".format(self.liquidTemperature.read_mc()))
        self.heaterLabel.config(text="Heater: {}".format(self.heater))
        self.colorSensorLabel.config(text="Color Sensor: {}".format(self.color))
        self.sirupPumpLabel.config(text="Sirup Pump: {}".format(self.sirupPumpValue))
        self.sirupValveLabel.config(text="Sirup Valve: {}".format(self.sirupValveValue))
        self.waterPumpLabel.config(text="Water Pump: {}".format(self.waterPumpValue))
        self.waterValveLabel.config(text="Water Valve: {}".format(self.waterValveValue))
        self.cupPresentLabel.config(text="Is a cup present: {}".format(self.iscupPresent))
        self.greenLedLabel.config(text="Is green led on: {}".format(self.greenLed))
        self.yellowLedLabel.config(text="Is yellow led on: {}".format(self.yellowLed))
        self.lcdValueLabel.config(text="LCD Value: {}".format(self.lcd))

        ## Log updated variables
        self.log.addSensorInfoLine("waterlevelSensorLabel", self.waterLevel)
        self.log.addSensorInfoLine("Liquid temperature", self.liquidTemperature)
        self.log.addSensorInfoLine("heater", self.heater)
        self.log.addSensorInfoLine("color", self.color)
        self.log.addSensorInfoLine("sirupPumpLabelValue", self.sirupPumpValue)
        self.log.addSensorInfoLine("sirupValveLabelValue", self.sirupValveValue)
        self.log.addSensorInfoLine("waterPumpLabelValue", self.waterPumpValue)
        self.log.addSensorInfoLine("waterValveLabelValue", self.waterValveValue)
        self.log.addSensorInfoLine("is cup present", self.iscupPresent)
        self.log.addSensorInfoLine("green led on", self.greenLed)
        self.log.addSensorInfoLine("yellow led on", self.yellowLed)
        self.log.addSensorInfoLine("lcd", self.lcd)