import unittest
from unittest import TestCase
from trendfollowing.extrema import n_day_highs, n_day_lows

import numpy as np

__author__ = 'nate'

class ExtremaTest(TestCase):
    def test_should_return_empty_highs(self):
        highs = n_day_highs(np.ma.zeros(0), 10)
        self.assertEqual(0, len(highs))

    def test_should_return_high_for_previous_n_days(self):
        prices = np.ma.zeros(20)
        prices[0] = 2.0
        highs = n_day_highs(prices, 10)
        self.assertEqual(2.0, highs[10])

        for i in range(11, 20):
            self.assertEquals(0, highs[i])
        
    def test_should_mask_first_n_days_for_highs(self):
        prices = np.ma.zeros(20)
        prices[9] = 1
        highs = n_day_highs(prices, 10)
        for i in range(0, 10):
            self.assertTrue(highs[i].mask)

        for i in range(10, 20):
            self.assertEqual(1, highs[i])

    def test_should_return_empty_lows(self):
        highs = n_day_highs(np.ma.ones(0), 10)
        self.assertEqual(0, len(highs))

    def test_should_return_low_for_previous_n_days(self):
        prices = np.ma.ones(20)
        prices[0] = 0
        lows = n_day_lows(prices, 10)
        self.assertEqual(0, lows[10])

        for i in range(11, 20):
            self.assertEquals(1.0, lows[i])

    def test_should_mask_first_n_days_for_lows(self):
        prices = np.ma.zeros(20)
        prices[9] = 1
        highs = n_day_highs(prices, 10)
        for i in range(0, 10):
            self.assertTrue(highs[i].mask)

        for i in range(10, 20):
            self.assertEqual(1, highs[i])

    def test_should_return_highs_with_same_size_as_prices(self):
        prices = np.ma.zeros(20)
        highs = n_day_highs(prices, 10)
        self.assertEqual(20, len(highs))

    def test_should_return_lows_with_same_size_as_prices(self):
        prices = np.ma.zeros(20)
        highs = n_day_lows(prices, 10)
        self.assertEqual(20, len(highs))

if __name__=="__main__":
    unittest.main()

