#!/usr/bin/python
import numpy as np
from numpy import array, float32
import datetime
import unittest

from unittest import TestCase
from trendfollowing.breakouts import get_new_highs, get_new_lows
from trendfollowing.timeseries import TimeSeries

__author__ = 'nate'

class BreakoutsTest(TestCase):
    def setUp(self):
        prices = [2,2,2,2,3,2,2,3,4,4,5,3,2,1]
        #data = [[(datetime.date(2011, 1, i+1), prices[i])] for i in range(14)]
        #print data
        #arr = array(data, dtype=[('date', datetime.date), ('adj_close', 'float32')])            
        #r = arr.view(np.recarray)

        data = np.zeros(14, dtype=[('date', datetime.date), ('adj_close', '<f8')])
        for i in range(14):
            data['date'][i] = datetime.date(2011, 1, i+1)            
            data['adj_close'][i] = prices[i]

        r = data.view(np.recarray)        
        self.timeseries = TimeSeries(r)

    def test_should_return_new_ten_day_high(self):
        new_highs = get_new_highs(self.timeseries, 10)
        for high in new_highs:
            print "New 10-day high on %s: %f" % (str(high.date), high.price)

        self.assertEquals(1, len(new_highs))
        self.assertEquals(5, new_highs[0].price)
    
    def test_get_new_highs_should_return_empty_for_insufficient_data(self):
        new_highs = get_new_highs(self.timeseries, 20)
        self.assertEquals(0, len(new_highs))

    def test_get_new_lows_should_return_empty_for_insufficient_data(self):
        new_lows = get_new_lows(self.timeseries, 20)
        self.assertEquals(0, len(new_lows))
    
    def test_is_new_low_should_return_false_for_insufficient_data(self):
        new_lows = get_new_lows(self.timeseries, 10)
        for low in new_lows:
            print "New 10-day low on %s: %f" % (str(low.date), low.price)
        self.assertEquals(1, len(new_lows))
        self.assertEquals(1, new_lows[0].price)

if __name__=="__main__":
    unittest.main()
