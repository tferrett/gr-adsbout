# Copyright 2020 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

########################################################################
# Check if there is C++ code at all
########################################################################
if(NOT adsbout_sources)
    MESSAGE(STATUS "No C++ sources... skipping python bindings")
    return()
endif(NOT adsbout_sources)

########################################################################
# Check for pygccxml
########################################################################
GR_PYTHON_CHECK_MODULE_RAW(
    "pygccxml"
    "import pygccxml"
    PYGCCXML_FOUND
    )

include(GrPybind)

########################################################################
# Python Bindings
########################################################################

list(APPEND adsbout_python_files
    python_bindings.cc)

GR_PYBIND_MAKE_OOT(adsbout
   ../..
   gr::adsbout
   "${adsbout_python_files}")

# copy bindings extension for use in QA test module
add_custom_command(TARGET adsbout_python POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:adsbout_python>
    ${CMAKE_BINARY_DIR}/test_modules/adsbout/
)

install(TARGETS adsbout_python DESTINATION ${GR_PYTHON_DIR}/adsbout COMPONENT pythonapi)
