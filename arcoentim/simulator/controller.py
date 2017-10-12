from tkinter import *
import gui

class controller():
    userInterface = gui.gui

    ## Control variables
    hwInterface = gui.sharedVariables()

    # Variables for amounts
    userLemonadeValue = "0"
    userWaterValue = "0"
    userSelectLemonade = True  # True = lemonade, False = water
    userStartMixing = False

    def keypadButton(self, buttonValue):
        if buttonValue != "":
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
                                    '*': lambda: self.__setattr__("iscupPresent", "No"), # Take the cup away from the simulator
                                    '#': lambda: self.__setattr__("iscupPresent", "Yes"), # Put the cup back into the simulator
                                    'A': lambda: self.__setattr__("userSelectLemonade", False), # Select water amount
                                    'B': lambda: self.__setattr__("userSelectLemonade", True), # Select lemonade amount
                                    'C': lambda: self.__setattr__("userStartMixing", True), # Start mixing
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
        self.hwInterface.emptyLcd()
        self.keypadButton(self.hwInterface.getc("keypad"))

        ## Check if a cup is in the machine
        if not self.hwInterface.get("isCupPresent"):
            self.hwInterface.set("sirupPump", 0)
            self.hwInterface.set("sirupValve", 1)
            self.hwInterface.set("waterPump", 0)
            self.hwInterface.set("waterValve", 1)
            self.hwInterface.putSting("lcd", "Plz put a cup in the machine")

        ## If the cup is present start checking some other things
        elif self.hwInterface.get("isCupPresent"):
            if self.userStartMixing:
                self.hwInterface.putSting("lcd", "Pouring your drink\nSelected amounts Water: " + str(int(self.userWaterValue)) + " Lemonade: " + str(int(self.userLemonadeValue)))
                if self.hwInterface.read_mm() < int(self.userLemonadeValue):
                    self.hwInterface.putSting("lcd", "\nNow pouring: lemonade")
                    self.hwInterface.set("sirupPump", 1)
                    self.hwInterface.set("sirupValve", 0)
                    self.hwInterface.set("waterPump", 0)
                    self.hwInterface.set("waterValve", 1)

                elif self.hwInterface.read_mm() >= int(self.userLemonadeValue) and self.hwInterface.read_mm() < int(self.userWaterValue) + int(self.userLemonadeValue):
                    self.hwInterface.set("sirupPump", 0)
                    self.hwInterface.set("sirupValve", 1)
                    self.hwInterface.set("waterPump", 1)
                    self.hwInterface.set("waterValve", 0)
                    self.hwInterface.putSting("lcd", "\nNow pouring: water")

                else:
                    self.hwInterface.putString("lcd", "Drink has been poured")
                    self.hwInterface.set("sirupPump", 0)
                    self.hwInterface.set("sirupValve", 1)
                    self.hwInterface.set("waterPump", 0)
                    self.hwInterface.set("waterValve", 1)
                    self.userStartMixing = False
                    self.userWaterValue = "0"
                    self.userLemonadeValue = "0"

            elif not self.userStartMixing:
                self.hwInterface.putSting("lcd", "Waiting for start(C) or values(A, B)\nSelected amounts Water: " + str(int(self.userWaterValue)) + " Lemonade: " + str(int(self.userLemonadeValue)))
                self.hwInterface.set("sirupPump", 0)
                self.hwInterface.set("sirupValve", 1)
                self.hwInterface.set("waterPump", 0)
                self.hwInterface.set("waterValve", 1)
                if self.userSelectLemonade:
                    self.hwInterface.putSting("lcd", "\nChanging lemonade now")
                else:
                    self.hwInterface.putSting("lcd", "\nChanging water now")