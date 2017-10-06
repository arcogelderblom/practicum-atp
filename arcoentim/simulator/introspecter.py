from unittest import *
import doctest
import io
import inspect
from contextlib import redirect_stdout

import class_demo

class inspector():
    itemTypes = {}

    def __init__(self, moduleName):
        self.items = dir(moduleName)
        self.moduleName = moduleName

    def sortIntoTypes(self):
        for item in self.items:
            typeOfItem = type(eval('self.moduleName.' + item)).__name__
            if typeOfItem in self.itemTypes:
                self.itemTypes[typeOfItem].append(item)
            else:
                self.itemTypes[typeOfItem] = [item]

    def getdoc(self, name):
        return inspect.getdoc(name)

    def signature(self, name):
        return inspect.signature(name)

## put your module name in the class creator and run the code
inspectt = inspector(class_demo)
inspectt.sortIntoTypes()
print(inspectt.itemTypes)