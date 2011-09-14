import datetime
import unittest
from unittest import TestCase

from trendfollowing.timeseries import TimeSeries
import matplotlib.mlab as mlab
import matplotlib.finance as finance
import numpy as np

class TimeSeriesTest(TestCase):
    def setUp(self):
        data = np.zeros(30, dtype=[('date', datetime.date), ('adj_close', '<f8')])

        self.start_date = datetime.date(2011, 1, 1)
        for i in range(0,30):
            data['date'][i] = datetime.date(2011, 1, i+1)            
            data['adj_close'][i] = i

        r = data.view(np.recarray)        
        self.timeseries = TimeSeries(r)
        
    def test_get_data(self):
        d = self.timeseries.get_data(datetime.date(2011, 1, 3))
        print d

    def test_get_dates(self):
        print self.timeseries.arr['date']

    def test_should_be_iterable(self):
        for t in self.timeseries:
            pass

    def test_each_element_should_have_date_and_adj_close(self):
        for t in self.timeseries:
            self.assertTrue(isinstance(t['date'],datetime.date))
            self.assertTrue(isinstance(t['adj_close'],float))

    def test_get_item_should_return_record(self):
        t = self.timeseries[0]    
        print t

    def test_get_item_should_return_struct(self):
        t = self.timeseries[0]    
        print t        
        date = t['date']
        print "date: %s" % str(date)

    def test_with_new_field_should_return_new_timeseries(self):
        
        t = self.timeseries.with_new_field('_55_day_high', [i for i in range(30)])
        self.assertEquals(30, len(t))
        self.assertEquals(0.0, t['_55_day_high'][0])
        self.assertEquals(29, t['_55_day_high'][29])
        fields = t.__get_field_names__()
        self.assertTrue('_55_day_high' in fields)
        self.assertTrue('date' in fields)
        for i in range(30):
            self.assertFalse(t.mask['_55_day_high'][i])
            self.assertFalse(t.mask['_55_day_high'][i])

    def test_with_new_field_should_mask_data(self):
        def mask_n_days_fn(r):
            for i in range(10):
                r.mask[i]['_55_day_high']=True
        t = self.timeseries.with_new_field('_55_day_high', [i for i in range(30)], mask_fn=mask_n_days_fn)
        print t.arr
        self.assertEquals(30, len(t))
        for i in range(10):
            self.assertTrue(t.mask['_55_day_high'][i])
        for i in range(10, 30):
            self.assertFalse(t.mask['_55_day_high'][i])
        for i in range(30):
            self.assertFalse(t.mask['date'][i])

        print t.arr
if __name__=="__main__":
    unittest.main()

                                 

