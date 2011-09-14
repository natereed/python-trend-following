#!/usr/bin/python

import datetime
import unittest
from unittest import TestCase
from trendfollowing.timeseries import TimeSeries
from trendfollowing.extrema import n_day_highs_for_time_series
import numpy as np

class TimeSeriesExtremaTest(TestCase):
    def setUp(self):
        data = np.zeros(30, dtype=[('date', '|O4'), ('open', '<f8'), ('high', '<f8'), ('low', '<f8'), ('close', '<f8'), ('volume', '<i4'), ('adj_close', '<f8')])
        
        self.start_date = datetime.date(2011, 1, 1)
        for i in range(0,30):
            data['date'][i] = datetime.date(2011, 1, i+1)
            data['open'][i] = i
            data['close'][i] = i
        recarray = data.view(np.recarray)
        self.timeseries = TimeSeries(recarray)
                
    def test_should_return_highs_for_previous_10_days(self):
        highs = n_day_highs_for_time_series(self.timeseries, 10, 'close')
        fields = highs.__get_field_names__()
        print "*** fields: "
        print fields

        print "***highs: " 
        print highs
        self.assertEquals(30, len(highs))

        #d = datetime.date(2011, 1, 1)
        #ts_data = highs.get_data(d)
        #print "data: "
        #print ts_data

        for i in range(10):
            self.assertTrue(highs[i]['10_period_high_close'].mask)
            
        #self.assertTrue(ts_data['10_period_high_close'].mask)
        
#        d = datetime.date(2011, 1, 10)
#        ts_data = highs.get_data(d)

        #d = datetime.date(2011, 1, 11)
        #ts_data = highs.get_data(d)
        
        print "Day 10 10 day high: " 
        print highs.arr[10]['10_period_high_close']
        print "mask: "
        print highs.arr[10].mask
        print "item: " 
        print highs.arr.item(10)
        print "data:"
        print highs.arr.item(10)[7]

        self.assertEquals(9.0, highs.arr.item(10)[7])

        d = datetime.date(2011, 1, 30)
        ts_data = highs.get_data(d)
        self.assertEquals(29.0, ts_data['close'])
        self.assertEquals(28.0, ts_data['10_period_high_close'])
        
if __name__=="__main__":
    unittest.main()

