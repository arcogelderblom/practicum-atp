#include "simulatorCPlusPlus.hpp"

simulatorCPlusPlus::simulatorCPlusPlus() {
    guiBase();
}

void simulatorCPlusPlus::guiBase() {
    updateValues();
    gui.attr("master").attr("mainloop")();
    try {
        gui.attr("master").attr("destroy")();
    }
    catch (...) {
    
    }
}
    
void simulatorCPlusPlus::updateValues() {
    sim.attr("updateLabels")();
    controller.attr("updateLabels")();
    gui.attr("master").attr("after")(100, py::cast(updateValues));
}