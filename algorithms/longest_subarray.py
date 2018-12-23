def longest_subarray(A):
    """ Takes an array of integers and finds the length of the longest subarray 
    all of whose entries are equal.

    Time: O(n)
    Space: O(1)
    """
    max_length, current_length, current_elem = float('-inf'), 0, None
    for elem in A:
        if elem == current_elem:
            current_length += 1
        else:
            current_elem = elem
            current_length = 1
        max_length = max(max_length, current_length)
    return max_length
