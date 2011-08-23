from trendfollowing.extrema import n_day_highs_for_time_series

class Breakout:
    def __init__(self, date, price, period):
        self.price = price
        self.date = date
        self.period = period    

class NewHigh(Breakout):
    def __init__(self, date, price, period):
        #super(NewHigh, date, price, period)
        Breakout.__init__(self, date, price, period)

class NewLow(Breakout):
    def __init__(self, date, price, period):
        Breakout.__init__(self, date, price, period)
    
def get_new_highs(ts, period):
    highs_timeseries = n_day_highs_for_time_series(ts, period, 'adj_close')

    new_highs = []
    for highs in highs_timeseries:
        # print "price for %s: %f" % (highs['date'], highs['adj_close'])    
        # print "previous high: %f" % (highs[str(period) + '_period_high_adj_close'])
        prev_high = highs[str(period) + '_period_high_adj_close']
        if (prev_high and highs['adj_close'] > prev_high):
            new_highs.append(NewHigh(highs['date'], highs['adj_close'], period))

    return new_highs

def get_new_lows(ts, period):
    return [NewLow(t.date, t['adj_close'], period) for t in ts if t['adj_close'] < n_day_low(ts, t.date, period)]    


    

