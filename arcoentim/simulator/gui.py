from tkinter import *
import lemonator
import math

class sharedVariables():
    usingHardware = True
    originalDistance = 88

    if usingHardware:
        hw = lemonator.lemonator(2)
        fluidLevel = hw.distance
        liquidTemperature = hw.temperature
        isCupPresent = hw.reflex
        sirupPump = hw.sirup_pump
        sirupValve = hw.sirup_valve
        waterPump = hw.water_pump
        waterValve = hw.water_valve
        keypad = hw.keypad
        lcd = hw.lcd
    else:
        fluidLevel = 88 # We measured the original distance that the sensor reads at 88 mm
        liquidTemperature = 10
        isCupPresent = False
        sirupPump = 0
        sirupValve = 1
        waterPump = 0
        waterValve = 1
        keypad = ""
    lcdString = "Nothing to report"

    ## Bools
    def set(self, variable, newValue):
        if sharedVariables.usingHardware:
            sharedVariables.__getattribute__(sharedVariables, variable).set(newValue)
        else:
            exec("sharedVariables." + str(variable) + ' = ' + str(newValue))

    def get(self, variable):
        if sharedVariables.usingHardware:
            if variable == "isCupPresent":
                return sharedVariables.__getattribute__(sharedVariables, variable).get()
        return sharedVariables.__getattribute__(sharedVariables, variable)



    ## Keypad
    def getCKeypad(self, variable):
        if sharedVariables.usingHardware:
            return sharedVariables.__getattribute__(sharedVariables, variable).getc()
        else:
            char = sharedVariables.keypad
            sharedVariables.keypad = ""
            return char


    def putCKeypad(self, value):
        ## This function cannot be used on the hardware variables
        if not sharedVariables.usingHardware:
            sharedVariables.keypad = value


    ## Lcd
    def putc(self, value):
        if sharedVariables.usingHardware:
            sharedVariables.lcd.putc(value)
        else:
            sharedVariables.lcdString += value

    def putString(self, newValue):
        if newValue != sharedVariables.lcdString:
            self.emptyLcd()
            sharedVariables.lcdString = newValue
            if sharedVariables.usingHardware:
                for c in newValue:
                    sharedVariables.lcd.putc(c) #self.putc(c)

    def emptyLcd(self):
        if sharedVariables.usingHardware:
            self.putc("\r")
            self.putc("\f")
        sharedVariables.lcdString = ""

    def getString(self):
        if not sharedVariables.usingHardware:
            return sharedVariables.lcdString

    ## Sensor
    def sensorMmToMl(self, value):
        return value * math.pi * 3.5**2

    def sensorMlToMm(self, value):
        return value / (math.pi * 3.5**2)

    def read_ml(self):
        if sharedVariables.usingHardware:
            return self.sensorMmToMl(self.originalDistance-sharedVariables.fluidLevel.read_mm())
        else:
            return self.sensorMmToMl(self.originalDistance-sharedVariables.fluidLevel)

    def write_ml(self, newValue):
        ## This function cannot be used on the hardware variables
        if not sharedVariables.usingHardware:
            sharedVariables.fluidLevel = self.originalDistance-self.sensorMlToMm(newValue)

class gui(Frame):
    master = None
    def __init__(self):
        self.master = Tk()
        Frame.__init__(self, self.master)
        self.pack()
        self.guiBase()

    def guiBase(self):
        self.master.title("Lemonator Simulator")
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(500, 500))
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack()
