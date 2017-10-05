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
root.mainloop()
root.destroy()#het lijkt er op dat het niet nodig is om het te destroyen


"""
levelValue = 0

from tkinter import *
root = Tk()
def clock():
    print("hello")
    levelSensor.config(text=level)
    #lab['text'] = time
    root.after(1000, clock) # run itself again after 1000 ms

level = "Level Sensor: {}".format(levelValue)
levelSensor = Label(root, text="Level Sensor: {}".format(level))
levelSensor.pack()

# run first time
clock()

root.mainloop()
"""