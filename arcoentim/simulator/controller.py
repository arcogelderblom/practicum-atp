import lemonator
from tkinter import *

class controller():
    hw = lemonator.lemonator(2)
    hwKeypad = hw.keypad

    def __init__(self, master):
        self.master = master

    def guiBase(self):
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

    def keypadButton(self, buttonValue):
        ## O# m
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
