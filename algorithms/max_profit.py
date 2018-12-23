def max_profit(prices):
    """ Compute the maximum profit that could be made by buying and then selling 
    one share of the stock.

    :params prices: list, denoting prices

    Time: O(n)
    Space: O(1)

    Key: the max profit that can be made by selling on each specific day is the 
    difference of the current price and the minimum seen so far.
    """
    min_so_far, max_profit = float('int'), 0.0
    for price in prices:
        max_profit_today = price - min_so_far
        max_profit = max(max_profit, max_profit_today)
        min_so_far = min(min_so_far, price)
    return max_profit
