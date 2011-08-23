#!/usr/bin/python

import datetime
import unittest
from unittest import TestCase
from trendfollowing.timeseries import TimeSeries
from trendfollowing.extrema import n_day_highs_for_time_series

class TimeSeriesExtremaTest(TestCase):
    def setUp(self):
        self.start_date = datetime.date(2011, 1, 1)
        data = []
        for i in range(0,30):
            data.append({'date' : datetime.date(2011, 1, i+1), 'open': i, 'close' : i})
        self.timeseries = TimeSeries(data)
        
    def test_should_return_highs_for_previous_10_days(self):
        highs = n_day_highs_for_time_series(self.timeseries, 10, 'close')
        print highs
        self.assertEquals(30, len(highs))

        d = datetime.date(2011, 1, 1)
        ts_data = highs.get_data(d)
        self.assertEquals(None, ts_data['10_period_high_close'])
    
        d = datetime.date(2011, 1, 10)
        ts_data = highs.get_data(d)
        self.assertEquals(None, ts_data['10_period_high_close'])
            
        d = datetime.date(2011, 1, 11)
        ts_data = highs.get_data(d)
        self.assertEquals(9.0, ts_data['10_period_high_close'])

        d = datetime.date(2011, 1, 30)
        ts_data = highs.get_data(d)
        self.assertEquals(29.0, ts_data['close'])
        self.assertEquals(28.0, ts_data['10_period_high_close'])
        
if __name__=="__main__":
    unittest.main()

