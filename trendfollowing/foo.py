__author__ = 'nate'

import numpy as np
from trendfollowing.arrayutils import maskarray

def n_day_highs(prices, n):
    return apply_extrema_function(max, prices, n)

def n_day_lows(prices, n):
    return apply_extrema_function(min, prices, n)
    
def apply_extrema_function(f, prices, n):
    values = np.ma.array(np.ma.zeros(len(prices)), mask=False)
    values.mask[:n] = True

    for i in range(n, len(prices)):
        values[i] = f(prices[i - n:i])

    return values
