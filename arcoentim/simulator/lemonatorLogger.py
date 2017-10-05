"""
import time
class logger:
    def __init__(self, filename):
        try:
            self.file = open(filename, "a")
            print("File with name:", filename, "opened")
        except:
            print("Could not open file")
    def __del__(self):
        try:
            self.file.close()
            print("File closed")
        except:
            print("Could not close file")

    def addLine(self, line):
        localtime = time.asctime(time.localtime(time.time()))
        self.file.write(localtime + ': ' + str(line) + '\n')

log = logger("somefile.txt")
log.addLine("somewarning")
log.addLine("error")
log.addLine("Sensor1 reports value " + str(10))
"""

import logging

class lemonatorLogger:

    #So far only these 4 types are included. More could be included once they are needed
    functions = {logging.INFO : logging.info,
                 logging.DEBUG : logging.debug,
                 logging.WARNING : logging.warning,
                 logging.ERROR : logging.ERROR}

    def __init__(self, filename):
        """
        A class creation call example would be:
        log = lemonatorLogger("log.txt")

        :param filename: The name of the file the information is put into
        """
        self.filename = filename

    def addSensorInfoLine(self, sensorName, value):
        """
        A function call example would be:
        addSensorInfoLine("someSensorName", 10)

        :param sensorName: The name or ID of the sensor
        :param value: The value it is reporting
        :return: No return variable
        """
        self.addLogLine(logging.INFO, " Sensor with ID: " + str(sensorName) + " reports value " + str(value))


    def addLogLine(self, typeOfLogItem, line):
        """
        A function call example would be:
        addLogLine(logging.WARNING, "The sensor is about to blow up")

        :param typeOfLogItem: The type of log line you want to print. Example: logging.ERROR
        :param line: The information to put into the log file
        :return: No return variable
        """
        logging.basicConfig(filename=self.filename, level=typeOfLogItem)
        self.functions[typeOfLogItem](line)


log = loggerTwo("newLog.log")
log.addSensorInfoLine("5x3bz", 10)