"""
File:       main.py
Part of:    simulator
Author:     Arco Gelderblom
Course:     Advanced Technical Programming
Teacher:    Huib Aldewereld
"""

import simulatorGui as Gui
from tkinter import *

root = Tk()
root.title("Lemonator Simulator")
app = Gui.Simulator(master=root)
app.updateValues()

#app.setLemonadeValue(5)
#app.setIsCupPresent(True)
#app.setWaterValue(7)
#app.setStartPouring()

root.mainloop()
try:
    root.destroy()
finally:
    print("App has been destroyed")
