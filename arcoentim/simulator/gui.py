from tkinter import *
import lemonator

class sharedVariables():
    usingHardware = False

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
        fluidLevel = 100
        liquidTemperature = 10
        isCupPresent = False
        sirupPump = 0
        sirupValve = 1
        waterPump = 0
        waterValve = 1
        keypad = ""
        lcd = "Nothing to report"

    ## Bools
    def set(self, variable, newValue):
        if sharedVariables.usingHardware:
            sharedVariables.__getattribute__(sharedVariables, variable).set(newValue)
        else:
            exec("sharedVariables." + str(variable) + ' = ' + str(newValue))

    def get(self, variable):
        if not sharedVariables.usingHardware:
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
            sharedVariables.lcd += value

    def putString(self, newValue):
        for c in newValue:
            self.putc(c)

    def emptyLcd(self):
        if sharedVariables.usingHardware:
            self.putc("\r")
            self.putc("\f")
        else:
            sharedVariables.lcd = ""

    def getString(self):
        if not sharedVariables.usingHardware:
            return sharedVariables.lcd

    ## Sensor
    def read_mm(self):
        if sharedVariables.usingHardware:
            return sharedVariables.fluidLevel.read_mm()
        else:
            return sharedVariables.fluidLevel

    def write_mm(self, newValue):
        ## This function cannot be used on the hardware variables
        if not sharedVariables.usingHardware:
            sharedVariables.fluidLevel = newValue

    #def read_mc(self, variable):
    #    if sharedVariables.usingHardware:
    #        return sharedVariables.__getattribute__(self, variable).read_mc()
    #    else:
    #        return sharedVariables.__getattribute__(self, variable)

    #def read_rgb(self):
    #    return 0


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