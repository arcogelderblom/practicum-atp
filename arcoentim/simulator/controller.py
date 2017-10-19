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
    originalDistance = 100
    originalDistanceSet = False

    def keypadButton(self, buttonValue):
        if buttonValue != "":
            print("Keypad value: ", buttonValue)
        try:
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
                                    '*': lambda: self.hwInterface.set("isCupPresent", False), # Take the cup away from the simulator
                                    '#': lambda: self.hwInterface.set("isCupPresent", True), # Put the cup back into the simulator
                                    'A': lambda: self.__setattr__("userSelectLemonade", False), # Select water amount
                                    'B': lambda: self.__setattr__("userSelectLemonade", True), # Select lemonade amount
                                    'C': lambda: self.__setattr__("userStartMixing", True), # Start mixing
                                    'D': lambda: print('D')}

            ## Execute watever the lambda function needs to
            correspondingActions[buttonValue]()
        except KeyError as err:
            pass
            #print(str(err))

    def assignDrinkValues(self, value):
        if self.userSelectLemonade:
            self.userLemonadeValue += value
        else:
            self.userWaterValue += value

    def updateLabels(self):
        ## Change variables
        self.hwInterface.emptyLcd()
        self.keypadButton(self.hwInterface.getCKeypad("keypad"))


        ## Check if a cup is in the machine
        if not self.hwInterface.get("isCupPresent"):
            self.hwInterface.set("sirupPump", 0)
            self.hwInterface.set("sirupValve", 1)
            self.hwInterface.set("waterPump", 0)
            self.hwInterface.set("waterValve", 1)
            self.hwInterface.putString("Plz put a cup in the machine")

        ## If the cup is present start checking some other things
        elif self.hwInterface.get("isCupPresent"):
            if self.userStartMixing:
                if self.originalDistanceSet:
                    currentLevel = self.originalDistance - self.hwInterface.read_mm()
                else:
                    self.originalDistance = self.hwInterface.read_mm()
                    self.originalDistanceSet = True

                self.hwInterface.putString("Pouring your drink\nSelected amounts Water: " + str(int(self.userWaterValue)) + " Lemonade: " + str(int(self.userLemonadeValue)))
                if currentLevel < int(self.userLemonadeValue):
                    self.hwInterface.putString("\nNow pouring: lemonade")
                    self.hwInterface.set("sirupPump", 1)
                    self.hwInterface.set("sirupValve", 0)
                    self.hwInterface.set("waterPump", 0)
                    self.hwInterface.set("waterValve", 1)

                elif currentLevel >= int(self.userLemonadeValue) and self.hwInterface.read_mm() < int(self.userWaterValue) + int(self.userLemonadeValue):
                    self.hwInterface.set("sirupPump", 0)
                    self.hwInterface.set("sirupValve", 1)
                    self.hwInterface.set("waterPump", 1)
                    self.hwInterface.set("waterValve", 0)
                    self.hwInterface.putString("\nNow pouring: water")

                else:
                    self.hwInterface.set("sirupPump", 0)
                    self.hwInterface.set("sirupValve", 1)
                    self.hwInterface.set("waterPump", 0)
                    self.hwInterface.set("waterValve", 1)
                    self.userStartMixing = False
                    self.userWaterValue = "0"
                    self.userLemonadeValue = "0"
                    self.hwInterface.write_mm(100)
                    self.originalDistanceSet = False

            elif not self.userStartMixing:
                self.hwInterface.putString("Waiting for start(C) or values(A, B)\nSelected amounts Water: " + str(int(self.userWaterValue)) + " Lemonade: " + str(int(self.userLemonadeValue)))
                self.hwInterface.set("sirupPump", 0)
                self.hwInterface.set("sirupValve", 1)
                self.hwInterface.set("waterPump", 0)
                self.hwInterface.set("waterValve", 1)
                if self.userSelectLemonade:
                    self.hwInterface.putString("\nChanging lemonade now")
                else:
                    self.hwInterface.putString("\nChanging water now")
