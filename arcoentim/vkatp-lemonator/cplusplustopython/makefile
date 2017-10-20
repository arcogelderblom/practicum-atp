#############################################################################
#
# Project Makefile
#
# (c) Wouter van Ooijen (www.voti.nl) 2016
#
# This file is in the public domain.
# 
#############################################################################

PROJECT := main

# source files in this project (main.cpp is automatically assumed)
SOURCES := rs232.c controllerCPlusPlus.cpp

# header files in this project
HEADERS := controllerCPlusPlus.hpp

# other places to look for files for this project
SEARCH  := 

# set RELATIVE to the next higher directory and defer to the Makefile.due
RELATIVE := $(RELATIVE)../
include $(RELATIVE)Makefile.native
