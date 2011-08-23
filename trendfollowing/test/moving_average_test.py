import numpy
import unittest
from unittest import TestCase
from trendfollowing.moving_average import calculate_moving_average

__author__ = 'nate'

class MovingAverageTest(TestCase):

    def setUp(self):
        self.prices = numpy.ma.zeros(10)
        for i in range(1,10):
            j = 10 % i
            if j > 0:
                self.prices[i] = 10 - j
            else:
                self.prices[i] = i

    def test_prices_cannot_be_empty(self):
        self.prices = numpy.ma.zeros(0)
        self.assertRaises(ValueError, calculate_moving_average, prices=self.prices, n=10)

    def test_should_mask_n_days_of_data(self):
        self.prices = numpy.ma.zeros(10)
        ma = calculate_moving_average(prices=self.prices, n=5)
        for i in range(0, 5):
            self.assertTrue(ma[i].mask)
        for i in range(6,10):
            self.assertTrue(ma[i] == 0)

    def test_should_return_averages_for_n_days_of_prices(self):
        self.prices = numpy.ma.zeros(10)
        ma = calculate_moving_average(prices=self.prices, n=10, mask=False)
        for i in range(0, 10):
            self.assertTrue(ma[i]==0)

    def test_should_return_averages_for_n_greater_than_prices(self):
        self.prices = numpy.ma.zeros(10)
        ma = calculate_moving_average(prices=self.prices, n=11, mask=False)
        self.assertEquals(10, len(ma))
        for i in range(0, 10):
            self.assertTrue(ma[i]==0)

if __name__=="__main__":
    unittest.main()

