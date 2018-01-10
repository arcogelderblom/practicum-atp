#ifndef SIMULATORCPLUSPLUS_HPP
#define SIMULATORCPLUSPLUS_HPP

#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#include "../pybind11/include/pybind11/pybind11.h"
#pragma GCC diagnostic pop

namespace py = pybind11;

class simulatorCPlusPlus {
private:
    py::object controller = py::module::import("controller").attr("controller")();
    py::object sim = py::module::import("simulatorGui").attr("simulatorGui")();
    py::object gui = py::module::import("gui").attr("gui")();
public:
    simulatorCPlusPlus();
    void guiBase();
    void updateValues();
};

#endif // SIMULATORCPLUSPLUS_HPP
