#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#include <../pybind11/include/pybind11/pybind11.h>
#include <../pybind11/include/pybind11/embed.h>
#include <../pybind11/include/pybind11/eval.h>
#pragma GCC diagnostic pop
#include <Python.h>
#include <iostream>

#include "simulatorCPlusPlus.hpp"
#include "controllerCPlusPlus.hpp"

namespace py = pybind11;

int main(void) {
    // Weird hack to make pybind actually work.
    Py_Initialize();
    wchar_t wstr[32];
    wchar_t* args = {wstr};
    std::mbstowcs(wstr, "lemonator", 9);
    PySys_SetArgv(1, &args);
    
    py::object sim = py::module::import("simulator").attr("simulator")(false);
    controllerCPlusPlus control;
    
    //simulatorCPlusPlus simulator;
}