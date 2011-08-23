__author__ = 'nate'

import numpy as np

def _maskarray(x, n):
    maskedarray = np.ma.array(x, mask=False)
    maskedarray.mask[:n] = True
    return maskedarray


def moving_average(prices, n, type='simple', mask=True):
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


def relative_strength(prices, n=14):
    """
    compute the n period relative strength indicator
    http://stockcharts.com/school/doku.php?id=chart_school:glossary_r#relativestrengthindex
    http://www.investopedia.com/terms/r/rsi.asp
    """

    deltas = np.diff(prices)
    seed = deltas[:n + 1]
    up = seed[seed >= 0].sum() / n
    down = -seed[seed < 0].sum() / n
    rs = up / down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100. / (1. + rs)

    for i in range(n, len(prices)):
        delta = deltas[i - 1] # cause the diff is 1 shorter

        if delta > 0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up * (n - 1) + upval) / n
        down = (down * (n - 1) + downval) / n

        rs = up / down
        rsi[i] = 100. - 100. / (1. + rs)

    return rsi


def moving_average_convergence(x, nslow=26, nfast=12):
    """
    compute the MACD (Moving Average Convergence/Divergence) using a fast and slow exponential moving avg'
    return value is emaslow, emafast, macd which are len(x) arrays
    """
    emaslow = moving_average(x, nslow, type='exponential')
    emafast = moving_average(x, nfast, type='exponential')
    return emaslow, emafast, emafast - emaslow


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
