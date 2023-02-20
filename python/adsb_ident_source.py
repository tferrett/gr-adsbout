#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2023 gr-adsbout author.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
from gnuradio import gr
from .adsb_encoder import gen_ident

class adsb_ident_source(gr.sync_block):
    """
    docstring for block adsb_ident_source
    """
    def __init__(self, ec, icao, callsign):
        gr.sync_block.__init__(self,
            name="adsb_ident_source",
            in_sig=None,
            out_sig=[numpy.int8])
        self.ec = ec
        self.icao = icao
        self.callsign = callsign
        self.data = gen_ident(self)

        

    def work(self, input_items, output_items):
        out = output_items[0]
        try:
            self.data[out.shape[0]]
            out[:] = self.data[:out.shape[0]]
            self.data = self.data[out.shape[0]:]
        except IndexError:
            self.data = self.data + gen_ident(self)
        return len(output_items[0])
