// dummy main to convince the script that this is a bmptk project
#include "controllerCPlusPlus.hpp"

int main(void) {
    controllerCPlusPlus controller;
    while true {
        controller.updateLabels();
    }
}