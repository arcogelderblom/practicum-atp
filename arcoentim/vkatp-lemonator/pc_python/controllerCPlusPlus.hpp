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
    py::object hwInterface = sharedVariables()
    
    std::string userLemonadeValue = "0";
    std::string userWaterValue = "0";
    bool userSelectLemonade = true;
    bool userStartMixing = false;
    int originalDistance = 100;
    int currentLevel = 0;
    
    std::map buttonActions<char, std::function<void()>> = {
        '1' : [&](){ assignDrinkValues('1') },
        '2' : [&](){ assignDrinkValues('2') },
        '3' : [&](){ assignDrinkValues('3') },
        '4' : [&](){ assignDrinkValues('4') },
        '5' : [&](){ assignDrinkValues('5') },
        '6' : [&](){ assignDrinkValues('6') },
        '7' : [&](){ assignDrinkValues('7') },
        '8' : [&](){ assignDrinkValues('8') },
        '9' : [&](){ assignDrinkValues('9') },
        '0' : [&](){ assignDrinkValues('0') },
        '*' : [&](){ hwInterface.set("isCupPresent", false) },
        '#' : [&](){ hwInterface.set("isCupPresent", true)  },
        'A' : [&](){ userSelectLemonade = false },
        'B' : [&](){ userSelectLemonade = true },
        'C' : [&](){ userStartMixing = true },
        'D' : [&](){ }
    };
    
public:
    controllerCPlusPlus();
    ~controllerCPlusPlus();
    
    void keypadButton(char buttonValue);
    void assignDrinkValues(char value);
    void updateLabels(void);
};

#endif // CONTROLLERCPLUSPLUS_HPP
