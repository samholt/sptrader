#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2016 Bitquant Research Laboratories (Asia) Limited
#
# Released under Simplified BSD License
#
###############################################################################
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime
import time
from backtrader.feeds import feed
from backtrader.utils import date2num


class SharpPointCSVData(feed.CSVDataBase):
    '''
    Parses a self-defined CSV Data used for testing.

    Specific parameters:

      - ``dataname``: The filename to parse or a file-like object
      - ``product`` : Product id
    '''
    params = (('product', None),
              ('newdata', False),
              ('keepalive', False),
              ('debug', True))

    def start(self):
        super(SharpPointCSVData, self).start()
        if self.p.newdata:
            self.f.seek(0,2)

    def _load(self):
        if self.f is None:
            return False

        # Let an exception propagate to let the caller know
        while True:
            line = self.f.readline()
            if not line:
                if not self.p.keepalive:
                    return False
                else:
                    time.sleep(0.1)
                    continue
            else:
                line = line.rstrip('\n')
                if self.p.debug:
                    print(line)
                linetokens = line.split(self.separator)
                if linetokens[4] == self.p.product:
                    return self._loadline(linetokens)

    def islive(self):
        return self.p.keepalive

    def _loadline(self, linetokens):
        itoken = iter(linetokens)

        price = float(next(itoken))
        volume = float(next(itoken))
        dtnum = float(next(itoken))
        dt = datetime.datetime.fromtimestamp(dtnum)
        self.lines.datetime[0] = date2num(dt)
        self.lines.open[0] = price
        self.lines.high[0] = price
        self.lines.low[0] = price
        self.lines.close[0] = price
        self.lines.volume[0] = volume
        self.lines.openinterest[0] = 0.0
        return True


class SharpPointCSV(feed.CSVFeedBase):
    DataCls = SharpPointCSVData