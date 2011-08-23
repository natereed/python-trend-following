__author__ = 'nate'

import numpy as np
from trendfollowing.arrayutils import maskarray
from trendfollowing.timeseries import TimeSeries

def n_day_highs(prices, n):
    return apply_extrema_function(max, prices, n)

def n_day_lows(prices, n):
    return apply_extrema_function(min, prices, n)

def n_day_highs_for_time_series(ts, n, entry_name):
    return apply_extrema_function_to_timeseries(ts, max, entry_name, str(n) + '_period_high_' + entry_name, n)

def n_day_lows_for_time_series(ts, n, entry_name):
    return apply_extrema_function_to_timeseries(ts, min, entry_name, str(n) + '_period_low_' + entry_name, n)

def apply_extrema_function(f, prices, n):
    values = np.ma.array(np.ma.zeros(len(prices)), mask=False)
    values.mask[:n] = True

    for i in range(n, len(prices)):
        values[i] = f(prices[i - n:i])

    return values

def apply_extrema_function_to_timeseries(timeseries, extrema_func, x_entry_name, y_entry_name, n):

    # new timeseries data - will contain the elements in ts_input plus the resulting values from applying the function applied to input
    # eg.
    # [{'date' : '01-01-15', 'open' : 1, 'close' : 2}...] => [{'date' : '01-01-15', 'open' : 1, 'close' : 2, 'extrema' => 2}]

    prices = []
    for tdata_input in timeseries:
        prices.append(tdata_input[x_entry_name])

    extrema = apply_extrema_function(extrema_func, prices, n)
    
    out_data = []
    index = min(n, len(timeseries))

    for i in range(0, index):
        tdata_input = timeseries[i]
        tdata_output = tdata_input.copy()
        tdata_output[y_entry_name] = None
        out_data.append(tdata_output)
    
    for i in range(index, len(timeseries)):
        tdata_input = timeseries[i]
        tdata_output = tdata_input.copy()
        tdata_output[y_entry_name] = extrema[i]
        out_data.append(tdata_output)

    return TimeSeries(out_data)


