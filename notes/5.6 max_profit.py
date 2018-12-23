"""
Write a program that takes an array denoting the daily stock price, and returns the 
maximum profit that could be made by buying and then selling one share of that stock.
There is no need to buy if no profit is possible. You must buy before you sell.

Solution.
The maximum profit we can gain is the difference between the current entry and the
minimum value we have seen so far.

Time O(n),
Space O(1)
"""

def buy_and_sell(prices):
    min_so_far, max_profit = float('inf'), 0.0
    for price in prices:
        max_profit_sell_today = price - min_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_so_far = min(min_so_far, price)
    return max_profit


def max_subarray(A):
    max_length, current_elem, current_length = float('-inf'), None, 0
    for a in A:
        print("a: {}, current_elem: {}, current_length: {}".format(a, current_elem, current_length))
        if a == current_elem:
            current_length += 1
        else:
            current_elem = a
            current_length = 1
        max_length = max(max_length, current_length)
    return max_length

from random import randint
for j in range(5):
    A = [randint(0, 3) for i in range(20)]
    print(A)
    print(max_subarray(A))

