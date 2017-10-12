from tkinter import *
import lemonator

class sharedVariables():
    usingHardware = False
    if usingHardware:
        hw = lemonator.lemonator(2)
        fluidLevel = hw.distance
        isCupPresent = hw.reflex
        sirupPump = hw.sirup_pump
        sirupValve = hw.sirup_valve
        waterPump = hw.water_pump
        waterValve = hw.water_valve
        lcd = hw.lcd
    else:
        fluidLevel = 0
        isCupPresent = False
        sirupPump = 0
        sirupValve = 1
        waterPump = 0
        waterValve = 1
        lcd = "Nothing to report"

    ## Bools
    def set(self, variable, newValue):
        if sharedVariables.usingHardware:
            sharedVariables.__getattribute__(variable).set(newValue)
        else:
            sharedVariables.__setattr__(variable, newValue)

    def get(self, variable):
        if sharedVariables.usingHardware:
            return sharedVariables.__getattribute__(variable).get()
        else:
            return sharedVariables.__getattribute__(variable)

    ## Keypad
    def getc(self, variable):
        if sharedVariables.usingHardware:
            return sharedVariables.__getattribute__(variable).getc()
        else:
            return sharedVariables.__getattribute__(variable)

    ## Lcd
    def putc(self, value):
        if sharedVariables.usingHardware:
            sharedVariables.lcd.putc()
        else:
            sharedVariables.lcd += value

    def putString(self, newValue):
        for c in newValue:
            sharedVariables.putc(c)

    def emptyLcd(self):
        if sharedVariables.usingHardware:
            sharedVariables.putc('\r')
            sharedVariables.putc('\f')
        else:
            sharedVariables.lcd = ""

    ## Sensor
    def read_mm(self, variable):
        if sharedVariables.usingHardware:
            return sharedVariables.__getattribute__(variable).read_mm()
        else:
            return sharedVariables.__getattribute__(variable)

    def read_mc(self, variable):
        if sharedVariables.usingHardware:
            return sharedVariables.__getattribute__(variable).read_mc()
        else:
            return sharedVariables.__getattribute__(variable)

    def read_rgb(self):
        pass


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