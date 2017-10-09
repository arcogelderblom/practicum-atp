from tkinter import *
import lemonatorLogger
import operator
#import lemonator

class rgbColor():
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return '(' + str(self.r) + ',' + str(self.g) + ',' + str(self.b) + ')'

class Simulator(Frame):
    """
    ## HW variables with lemonator

    hw = lemonator.lemonator(2)
    waterLevel = hw.distance #The example shows this however i can not test it
    heater = hw.heather
    liquidTemperature = hw.temperature
    color = hw.color
    sirupPumpLabelValue = hw.sirup_pump
    sirupValveLabelValue = hw.sirup_valve
    waterPumpLabelValue = hw.water_pump
    waterValveLabelValue = hw.water_valve
    lcd = hw.lcd
    keypad = hw.keypad
    liquidTemperature = hw.temperature
    iscupPresentLabel = hw.reflex
    greenLed = hw.led_green
    yellowLed = hw.led_yellow
    """

    ## simulator variables
    waterLevel = 0
    liquidTemperature = 0
    heater = "Off"
    color = rgbColor(0, 0, 0)
    sirupPumpValue = 0
    sirupValveValue = 0
    waterPumpValue = 0
    waterValveValue = 0
    iscupPresent = "No"
    greenLed = "No"
    yellowLed = "No"
    lcd = "Plz put cup in machine\nand specify an amount (A and B keys)"

    # Variables for amounts
    userLemonadeValue = "0"
    userWaterValue = "0"
    userSelectLemonade = True # True = lemonade, False = water
    userStartMixing = False

    ## Logger
    log = lemonatorLogger.lemonatorLogger("log.txt")

    def __init__(self, master=None):
        self.master = master
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def updateValues(self):
        self.updateLabels()
        self.master.after(1000, self.updateValues)

    def assignDrinkValues(self, value):
        if self.userSelectLemonade:
            self.userLemonadeValue += value
        else:
            self.userWaterValue += value

    def keypadButton(self, buttonValue):
        ## Only a few have been added now the rest comes later when we know what to do with them
        correspondingActions = {1: lambda: self.assignDrinkValues("1"),
                                2: lambda: self.assignDrinkValues("2"),
                                3: lambda: self.assignDrinkValues("3"),
                                4: lambda: self.assignDrinkValues("4"),
                                5: lambda: self.assignDrinkValues("5"),
                                6: lambda: self.assignDrinkValues("6"),
                                7: lambda: self.assignDrinkValues("7"),
                                8: lambda: self.assignDrinkValues("8"),
                                9: lambda: self.assignDrinkValues("9"),
                                0: lambda: self.assignDrinkValues("0"),
                                '*': lambda: self.__setattr__("iscupPresent", "No"), # Take the cup away from the simulator
                                '#': lambda: self.__setattr__("iscupPresent", "Yes"), # Put the cup back into the simulator
                                'A': lambda: self.__setattr__("userSelectLemonade", False), # Select water amount
                                'B': lambda: self.__setattr__("userSelectLemonade", True), # Select lemonade amount
                                'C': lambda: self.__setattr__("userStartMixing", True), # Start mixing
                                'D': lambda: print('D')}

        ## Execute watever the lambda function needs to
        correspondingActions[buttonValue]()

    def createWidgets(self):
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format( 500, 500))
        ## Quit Button
        self.master.geometry()
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack()

        ## Label for level sensor
        self.levelSensorLabel = Label(self.master, text="Level Sensor: {} ml".format(self.waterLevel))
        self.levelSensorLabel.pack()

        ## Label for heather
        self.heaterLabel = Label(self.master, text="Heather: {}".format(self.heater))
        #self.heaterLabel.pack()

        ## Label for liquid temperature
        self.liquidLabel = Label(self.master, text="Liquid Temperature: {} celsius".format(self.liquidTemperature))
        #self.liquidLabel.pack()

        ## Label for color sensor
        self.colorSensorLabel = Label(self.master, text="Color Sensor: {}".format(self.color))
        #self.colorSensorLabel.pack()

        ## Label for sirup pump
        self.sirupPumpLabel = Label(self.master, text="Sirup Pump: {}".format(self.sirupPumpValue))
        self.sirupPumpLabel.pack()

        ## Label for sirup valve
        self.sirupValveLabel = Label(self.master, text="Sirup Valve: {}".format(self.sirupValveValue))
        self.sirupValveLabel.pack()

        ## Label for water pump
        self.waterPumpLabel = Label(self.master, text="Water Pump: {}".format(self.waterPumpValue))
        self.waterPumpLabel.pack()

        ## Label for water valve
        self.waterValveLabel = Label(self.master, text="Water Valve: {}".format(self.waterValveValue))
        self.waterValveLabel.pack()

        ## Cup present label
        self.cupPresentLabel = Label(self.master, text="Is a cup present: {}".format(self.iscupPresent))
        self.cupPresentLabel.pack()

        ## Green led
        self.greenLedLabel = Label(self.master, text="Is green led on: {}".format(self.greenLed))
        #self.greenLedLabel.pack()

        ## Yellow led
        self.yellowLedLabel = Label(self.master, text="Is yellow led on: {}".format(self.yellowLed))
        #self.yellowLedLabel.pack()

        ## LCD
        self.lcdValueLabel = Label(self.master, text="LCD Value: {}".format(self.lcd))
        self.lcdValueLabel.place(x=100, y=200)

        Button(self.master, text="1", command=lambda: self.keypadButton(1)).place(x=160, y=300)
        Button(self.master, text="2", command=lambda: self.keypadButton(2)).place(x=210, y=300)
        Button(self.master, text="3", command=lambda: self.keypadButton(3)).place(x=260, y=300)
        Button(self.master, text="4", command=lambda: self.keypadButton(4)).place(x=160, y=330)
        Button(self.master, text="5", command=lambda: self.keypadButton(5)).place(x=210, y=330)
        Button(self.master, text="6", command=lambda: self.keypadButton(6)).place(x=260, y=330)
        Button(self.master, text="7", command=lambda: self.keypadButton(7)).place(x=160, y=360)
        Button(self.master, text="8", command=lambda: self.keypadButton(8)).place(x=210, y=360)
        Button(self.master, text="9", command=lambda: self.keypadButton(9)).place(x=260, y=360)
        Button(self.master, text="0", command=lambda: self.keypadButton(0)).place(x=210, y=390)
        Button(self.master, text="*", command=lambda: self.keypadButton('*')).place(x=160, y=390)
        Button(self.master, text="#", command=lambda: self.keypadButton('#')).place(x=260, y=390)
        Button(self.master, text="A", command=lambda: self.keypadButton('A')).place(x=310, y=300)
        Button(self.master, text="B", command=lambda: self.keypadButton('B')).place(x=310, y=330)
        Button(self.master, text="C", command=lambda: self.keypadButton('C')).place(x=310, y=360)
        Button(self.master, text="D", command=lambda: self.keypadButton('D')).place(x=310, y=390)


    def updateLabels(self):
        ## Change variables
        if self.iscupPresent == "No":
            self.sirupPumpValue = 0
            self.sirupValveValue = 1
            self.waterPumpValue = 0
            self.waterValveValue = 1
            self.lcd = "Plz put a cup in the machine"
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
        self.liquidLabel.config(text="Liquid Temperature: {} celsius".format(self.liquidTemperature))
        self.heaterLabel.config(text="Heather: {} celsius".format(self.heater))
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


        """
        ## Update all variables
        self.waterLevel = self.hw.distance
        self.color = self.hw.color
        self.heater = self.hw.heather
        self.sirupPumpLabelValue = self.hw.sirup_pump
        self.sirupValveLabelValue = self.hw.sirup_valve
        self.waterPumpLabelValue = self.hw.water_pump
        self.waterValveLabelValue = self.hw.water_valve
        """

    def setLemonadeValue(self, newValue):
        self.userLemonadeValue = str(newValue)

    def setWaterValue(self, newValue):
        self.userWaterValue = str(newValue)

    def setStartPouring(self):
        self.userStartMixing = True

    def setIsCupPresent(self, newValue):
        if newValue:
            self.iscupPresent = "Yes"
        else:
            self.iscupPresent = "No"