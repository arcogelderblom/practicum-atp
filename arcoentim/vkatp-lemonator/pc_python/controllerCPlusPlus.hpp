#ifndef CONTROLLERCPLUSPLUS_HPP
#define CONTROLLERCPLUSPLUS_HPP

#include <string>
#include <map>
#include <functional>

#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#include "../pybind11/include/pybind11/pybind11.h"
#pragma GCC diagnostic pop

namespace py = pybind11;

class controllerCPlusPlus {
private:
    //py::object hwInterface = sharedVariables()
    
    std::string userLemonadeValue = "0";
    std::string userWaterValue = "0";
    bool userSelectLemonade = true;
    bool userStartMixing = false;
    int originalDistance = 100;
    int currentLevel = 0;
    
    std::map<char, std::function<void()>> buttonActions;
    
    //buttonActions['1'] = [&](){ assignDrinkValues('1') };
    //buttonActions['2'] = [&](){ assignDrinkValues('2') };
    //buttonActions['3'] = [&](){ assignDrinkValues('3') };
    //buttonActions['4'] = [&](){ assignDrinkValues('4') };
    //buttonActions['5'] = [&](){ assignDrinkValues('5') };
    //buttonActions['6'] = [&](){ assignDrinkValues('6') };
    //buttonActions['7'] = [&](){ assignDrinkValues('7') };
    //buttonActions['8'] = [&](){ assignDrinkValues('8') };
    //buttonActions['9'] = [&](){ assignDrinkValues('9') };
    //buttonActions['0'] = [&](){ assignDrinkValues('0') };
    //buttonActions['*'] = [&](){ hwInterface.set("isCupPresent", false) };
    //buttonActions['#'] = [&](){ hwInterface.set("isCupPresent", true)  };
    //buttonActions['A'] = [&](){ userSelectLemonade = false };
    //buttonActions['B'] = [&](){ userSelectLemonade = true };
    //buttonActions['C'] = [&](){ userStartMixing = true };
    //buttonActions['D'] = [&](){ };
    
public:
    controllerCPlusPlus();
    ~controllerCPlusPlus();
    
    void keypadButton(char buttonValue);
    void assignDrinkValues(char value);
    void updateLabels(void);
};

#endif // CONTROLLERCPLUSPLUS_HPP
