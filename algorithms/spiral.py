def matrix_in_spiral_order(square_matrix):
    """ Write a program which takes an n by n 2D array and return the spiral 
    ordering of the array. For example,

    1 2 3
    4 5 6 => 1 2 3 6 9 8 7 4 5 6
    7 8 9

    Time: O(n^2), 
    Space: O(1)
    """
    SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = x = y = 0
    spiral_ordering = []
    for _ in range(len(square_matrix) ** 2):
        spiral_ordering.append(square_matrix[x][y])
        square_matrix[x][y] = 0
        next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        if (next_x not in range(len(square_matrix))
                or next_y not in range(len(square_matrix))
                or square_matrix[next_x][next_y] == 0):
            direction = (direction + 1) & 3
            next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
        x, y = next_x, next_y
    return spiral_ordering


