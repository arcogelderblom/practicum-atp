#ifndef CONTROLLERCPLUSPLUS_HPP
#define CONTROLLERCPLUSPLUS_HPP

#include <string>
#include <map>
#include <functional>
#include <iostream>

#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#include "../pybind11/include/pybind11/pybind11.h"
#pragma GCC diagnostic pop

namespace py = pybind11;


class controllerCPlusPlus {
private:
    py::object guiFile = py::module::import("gui");
    py::object hwInterface = guiFile.attr("sharedVariables")();
    
    std::string userLemonadeValue = "0";
    std::string userWaterValue = "0";
    bool userSelectLemonade = true;
    bool userStartMixing = false;
    bool originalDistanceSet = true;
    int originalDistance = 100;
    int currentLevel = 0;
    
    std::map<char, std::function<void()>> buttonActions;
    
public:
    controllerCPlusPlus();
    
    void keypadButton(char buttonValue);
    void assignDrinkValues(char value);
    void updateLabels(void);
};

#endif // CONTROLLERCPLUSPLUS_HPP
