"""
Writing programming interview questions hasn't made me rich yet ... so I might
give up and start trading Apple stocks all day instead.

First, I wanna know how much money I could have made yesterday if I'd been
trading Apple stocks all day.

So I grabbed Apple's stock prices from yesterday and put them in a list called
stock_prices, where:

The indices are the time (in minutes) past trade opening time, which was 9:30am
local time.
The values are the price (in US dollars) of one share of Apple stock at that time.
So if the stock cost $500 at 10:30am, that means stock_prices[60] = 500.

Write an efficient function that takes stock_prices and returns the best profit
I could have made from one purchase and one sale of one share of Apple stock
yesterday.

For example:

  stock_prices = [10, 7, 5, 8, 11, 9]

get_max_profit(stock_prices)
# Returns 6 (buying for $5 and selling for $11)

Python 3.6
No "shorting"—you need to buy before you can sell. Also, you can't buy and sell in the same time step—at least 1 minute has to pass.
"""

def get_max_profit(stock_prices):
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for i range(1, len(stock_prices)):
        profit = stock_prices[i] - min_price
        max_profit = max(profit, max_profit)
        min_price = min(stock_prices[i], min_price)

    return max_profit

def get_best_buy_sell_times(stock_prices):
    buy_index = 0
    sell_index = 0
    prev_profit=stock_prices[sell_index] - stock_prices[buy_index]

    for i in range(i, len(stock_prices)):
        current_profit = stock_prices[i] - stock_prices[buy_index]
        if current_profit > prev_profit :
            sell_index =i
        if stock_prices[i] < stock_prices[buy_index]:
            buy_index = i

    return [buy_index, sell_index]

print get_max_profit([10, 7, 5, 8, 11, 9])
print get_max_profit([10, 7, 5, 2, 1, 0])
print get_best_buy_sell_times([10, 7, 5, 8, 11, 9])
print get_best_buy_sell_times([10, 7, 5, 2, 1, 0])


# Tests

import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


unittest.main(verbosity=2)
