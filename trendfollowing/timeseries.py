import matplotlib.mlab as mlab
import numpy as np
import numpy.ma.mrecords as mrecords

class TimeSeries:
    def __init__(self, arr):
        self.arr = arr
        self.date_index = dict()
        for i,d in enumerate(self.arr['date']):
            self.date_index[d] = i
        try:
            self.mask = arr.mask
        except AttributeError:
            self.mask = None

    def __iter__(self):
        return TimeSeriesIter(self)        
        
#    def __getattr__(self, name):
#        print "__getattr__(%s)" % name
#        return self.arr.name
    
    def __len__(self):
        return len(self.arr)

    def __get_field_names__(self):
        return [d[0] for d in self.arr.dtype.descr]

    def __getitem__(self, key):
        return self.arr[key]

    def get_data(self, date):
        i = self.date_index[date]        
        field_names = self.__get_field_names__()
        data = dict()
        for name in field_names:
            data[name] = self.arr[name][i]
        return data

    def with_new_field(self, name, data, mask_arr=None, mask_fn=None):
        recarray = self.arr.view(np.recarray)
        recarray = mlab.rec_append_fields(recarray, name, data)
        if mask_arr:
            data = np.ma.array(recarray, mask=mask_arr)
        else:
            data = recarray

        r = data.view(mrecords.mrecarray)       
        if mask_fn:
            mask_fn(r)

        return TimeSeries(r)

class TimeSeriesIter:
    def __init__(self, t):
        self.timeseries = t
        self.dateiter = t['date'].__iter__()
        self.index = 0

    def next(self):
        d = self.dateiter.next()
        return self.timeseries.get_data(d)

