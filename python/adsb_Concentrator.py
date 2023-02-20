#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2023 gr-adsbout author.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
from gnuradio import gr

class adsb_Concentrator(gr.basic_block):
    """
    docstring for block adsb_Concentrator
    """
    def __init__(self, gap, ninputs):
        gr.basic_block.__init__(self,
            name="adsb_Concentrator",
            in_sig=[numpy.int8 for i in range(ninputs)],
            out_sig=[numpy.int8])
        self.data = []
        self.gap = gap
        
    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items
        
        
    def general_work(self, input_items, output_items):
        out = output_items[0]

        try:
            self.data[out.shape[0]]
            out[:] = self.data[:out.shape[0]]
            self.data = self.data[out.shape[0]:]
        except IndexError:
            gap_array = [0 for _ in range(self.gap)]
            for i in range(len(input_items)):
                self.data = self.data + list(input_items[i]) + gap_array
                self.consume(i,len(input_items[i]))

        return len(output_items[0])
