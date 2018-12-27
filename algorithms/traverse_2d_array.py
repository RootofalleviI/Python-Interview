def number_of_ways(n, m):
    """ Return the number of ways to traverse a 2D array (top-left to bottom-right). 
    You must either go right or down. """
    
    def helper(x, y):
        if x == y == 0:
            return 1

        if number_of_ways[x][y] == 0:
            ways_top = 0 if x == 0 else helper(x - 1, y)
            ways_left = 0 if y == 0 else helper(x, y - 1)
            number_of_ways[x][y] = ways_top + ways_left

        return number_of_ways[x][y]

    number_of_ways = [[0] * m for _ in range(n)]
    return helper(n - 1, m - 1)
