class TimeSeries(list):
    def __init__(self, data):
        list.__init__(self, data)

        self.indexed_data = dict()
        for d in data:
            self.indexed_data[d['date']] = d

    def __iter__(self):
        return list.__iter__(self)

    def __getslice__(self, i, j):
        return TimeSeries(list.__getslice__(self, i, j))

    def get_data(self, date):
        return self.indexed_data[date]

    def get_index(self, date):
        for i, v in enumerate(self):
            if v['date'] == date:
                return i
        return None

    def get_start_index(self, i, period):
        return max(0, i - period)


        

        
        
