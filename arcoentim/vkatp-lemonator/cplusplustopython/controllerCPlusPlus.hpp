#ifndef CONTROLLERCPLUSPLUS_HPP
#define CONTROLLERCPLUSPLUS_HPP

#include <string>

#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#include "../pybind11/include/pybind11/pybind11.h"
#pragma GCC diagnostic pop

namespace py = pybind11;

class controllerCPlusPlus {
private:
    //py::module gui = py::module::import("gui");
    //py::object hwInterface = gui.attr("sharedVariables")();
    
    std::string userLemonadeValue = "0";
    std::string userWaterValue = "0";
    bool userSelectLemonade = true;
    bool userStartMixing = false;
    int originalDistance = 100;
    int currentLevel = 0;
    
public:
    controllerCPlusPlus();
    
    void keypadButton(char buttonValue);
    void assignDrinkValues(char value);
};

#endif // CONTROLLERCPLUSPLUS_HPP