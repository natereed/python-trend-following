#!/usr/bin/python

import datetime
import unittest

from unittest import TestCase
from trendfollowing.breakouts import get_new_highs, get_new_lows
from trendfollowing.timeseries import TimeSeries

__author__ = 'nate'

class BreakoutsTest(TestCase):
    def setUp(self):
        prices = [{'date' : datetime.date(2011, 1, 1), 'open' : 2, 'adj_close' : 2},
                  {'date' : datetime.date(2011, 1, 2), 'open' : 2, 'adj_close' : 2},
                  {'date' : datetime.date(2011, 1, 3), 'open' : 2, 'adj_close' : 2},
                  {'date' : datetime.date(2011, 1, 4), 'open' : 2, 'adj_close' : 2},
                  {'date' : datetime.date(2011, 1, 5), 'open' : 2, 'adj_close' : 3},
                  {'date' : datetime.date(2011, 1, 6), 'open' : 3, 'adj_close' : 2},
                  {'date' : datetime.date(2011, 1, 7), 'open' : 2, 'adj_close' : 2},
                  {'date' : datetime.date(2011, 1, 8), 'open' : 2, 'adj_close' : 3},
                  {'date' : datetime.date(2011, 1, 9), 'open' : 3, 'adj_close' : 4},
                  {'date' : datetime.date(2011, 1, 10), 'open' : 4, 'adj_close' : 4},
                  {'date' : datetime.date(2011, 1, 11), 'open' : 4, 'adj_close' : 5},
                  {'date' : datetime.date(2011, 1, 12), 'open' : 5, 'adj_close' : 3},
                  {'date' : datetime.date(2011, 1, 13), 'open' : 3, 'adj_close' : 2},
                  {'date' : datetime.date(2011, 1, 14), 'open' : 2, 'adj_close' : 1}]                  
        self.timeseries = TimeSeries(prices)

    def test_should_return_new_ten_day_high(self):
        new_highs = get_new_highs(self.timeseries, 10)
        for high in new_highs:
            print "New high on %s: %f" % (str(high.date), high.price)

        self.assertEquals(1, len(new_highs))
        self.assertEquals(5, new_highs[0].price)
    
    def test_should_return_empty_for_insufficient_data(self):
        new_highs = get_new_highs(self.timeseries, 20)
        self.assertEquals(0, len(new_highs))

    def test_is_new_low_should_return_false_for_insufficient_data(self):
#        self.assertFalse(is_new_low(self.prices, 10, 20))
        pass

    def test_should_return_true_for_new_ten_day_low(self):
#        self.assertTrue(is_new_low(self.prices, 13, 10))
        pass

if __name__=="__main__":
    unittest.main()
