__author__ = 'nate'

import numpy as np

def _maskarray(x, n):
    maskedarray = np.ma.array(x, mask=False)
    maskedarray.mask[:n] = True
    return maskedarray


def calculate_moving_average(prices, n, type='simple', mask=True):
    """
    compute an n period moving average.

    type is 'simple' | 'exponential'

    """
    prices = np.asarray(prices)
    if type == 'simple':
        weights = np.ones(n)
    else:
        weights = np.exp(np.linspace(-1., 0., n))

    weights /= weights.sum()

    averages = np.convolve(prices, weights, mode='full')[:len(prices)]
    if n >= len(prices):
        i = len(prices) - 1
    else:
        i = n
    averages[:i] = averages[i]

    if mask:
        return _maskarray(averages, i)
    else:
        return averages




