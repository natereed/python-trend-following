#!/usr/bin/python

import datetime
import unittest
from unittest import TestCase
from trendfollowing.timeseries import TimeSeries

class TimeSeriesTest(TestCase):
    def setUp(self):
        self.start_date = datetime.date(2011, 1, 1)
        self.data = []
        for i in range(0,30):
            self.data.append({'date' : datetime.date(2011, 1, i+1), 'open': i, 'close' : i})
        self.ts = TimeSeries(self.data)
                        
    def test_should_be_iterable(self):
        for t in self.ts:
            pass

    def test_should_be_same_length(self):    
        self.assertEqual(30, len(self.ts))

    def test_each_element_should_have_date(self):
        for t in self.ts:
            self.assertTrue(isinstance(t['date'],datetime.date))

    def test_should_return_data_given_date(self):
        data = self.ts.get_data(datetime.date(2011, 1, 1))
        self.assertEquals(data['date'], self.start_date)

    def test_should_return_array_slice(self):
        ts = self.ts[1:]
        self.assertEquals(ts[0]['date'], datetime.date(2011, 1, 2))
        self.assertEquals(29, len(ts))
    
    def test_get_index(self):
        print "timeseries %s" % self.ts
        print "get_index: %s " % self.ts.get_index
        print "date: %s" % datetime.date(2011,1,1)
        print "get_index(datetime(2011,1,1)) %s" % self.ts.get_index(datetime.date(2011,1,1))

        self.assertEquals(30, len(self.data))
        i = self.ts.get_index(datetime.date(2011, 1, 1))
        self.assertEquals(0, i)

        i = self.ts.get_index(datetime.date(2011, 1, 2))
        self.assertEquals(1, i)

        i = self.ts.get_index(datetime.date(2011, 1, 30))
        self.assertEquals(29, i)

#    def test_should_return_range(self):
#        ts = self.ts.get_range(datetime.date(2011, 1, 2), 10)
#        self.assertEquals(2, len(ts))
#        self.assertEquals(ts[0]['date'], datetime.date(2011, 1, 1))
 #       self.assertEquals(ts[1]['date'], datetime.date(2011, 1, 2))        

    def test_getslice(self):
        ts = self.ts.__getslice__(0, len(self.data))
        self.assertEquals(30, len(ts))

    def test_get_start_index_should_never_be_negative(self):
        i = self.ts.get_start_index(0, 10)
        self.assertEquals(0, i)

if __name__=="__main__":
    unittest.main()


        
