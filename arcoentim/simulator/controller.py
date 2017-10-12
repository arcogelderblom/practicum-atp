import lemonator
from tkinter import *
import gui
import simulatorGui

class controller():
    userInterface = gui.gui

    ## Control variables
    hwInterface = gui.sharedVariables()

    # Variables for amounts
    userLemonadeValue = "0"
    userWaterValue = "0"
    userSelectLemonade = True  # True = lemonade, False = water
    userStartMixing = False

    def __init__(self):
        self.guiBase()

    def guiBase(self):
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
        ## needs to be changed to setc() so the chars can be retreived with getc()
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
                                '*': lambda: setattr(self.sim,"iscupPresent", "No"), # Take the cup away from the simulator
                                '#': lambda: setattr(self.sim,"iscupPresent", "Yes"), # Put the cup back into the simulator
                                'A': lambda: setattr(self.sim,"userSelectLemonade", False), # Select water amount
                                'B': lambda: setattr(self.sim,"userSelectLemonade", True), # Select lemonade amount
                                'C': lambda: setattr(self.sim,"userStartMixing", True), # Start mixing
                                'D': lambda: print('D')}

        ## Execute watever the lambda function needs to
        correspondingActions[buttonValue]()

    def assignDrinkValues(self, value):
        if self.userSelectLemonade:
            self.userLemonadeValue += value
        else:
            self.userWaterValue += value

    def updateLabels(self):
        ## Change variables
        if not self.hwInterface.get("isCupPresent"):
            self.hwInterface.set("sirupPump", 0)
            self.hwInterface.set("sirupValve", 1)
            self.hwInterface.set("waterPump", 0)
            self.hwInterface.set("waterValve", 1)
            self.hwInterface.putSting("lcd", "Plz put a cup in the machine")
        elif self.hwInterface.get("isCupPresent"):
            if self.userStartMixing:
                self.lcd = "Pouring your drink\nSelected amounts Water: " + str(
                    int(self.userWaterValue)) + " Lemonade: " + str(int(self.userLemonadeValue))
                self.waterLevel += 1
                if self.waterLevel < int(self.userLemonadeValue):
                    self.lcd += "\nNow pouring: lemonade"
                    self.sirupValveValue = 0
                    self.sirupPumpValue = 1
                    self.waterPumpValue = 0
                    self.waterValveValue = 1

                elif self.waterLevel >= int(self.userLemonadeValue) and self.waterLevel < int(
                        self.userWaterValue) + int(self.userLemonadeValue):
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
                    # changin weglaten

            elif not self.userStartMixing:
                self.lcd = "Waiting for start(C) or values(A, B)\nSelected amounts Water: " + str(
                    int(self.userWaterValue)) + " Lemonade: " + str(int(self.userLemonadeValue))
                self.sirupPumpValue = 0
                self.sirupValveValue = 1
                self.waterPumpValue = 0
                self.waterValveValue = 1
                self.waterLevel = 0
                if self.userSelectLemonade:
                    self.lcd += "\nChanging lemonade now"
                else:
                    self.lcd += "\nChanging water now"