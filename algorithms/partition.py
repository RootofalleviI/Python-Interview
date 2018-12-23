def partition(A, i):
    """ Reorder an array such that all elements less than the pivot appear first,
    followed by elements equal to the pivot, followed by elements greater than the
    pivot. The original array is modified in-place. 

    :params A: list, the array to be reordered
    :params i: integer, index of the pivot entry
    
    Time complexity: O(n)
    Space complexity: O(1)

    Invariants:
    - A[:lower]: group of numbers that are less than the pivot.
    - A[lower:middle]: group of numbers that equal to the pivot.
    - A[middle:upper]: group of numbers that are unclassified.
    - A[upper:]: group of numbers that are greater than the pivot.

    Extra remarks:
    - A[middle]: the current processing element.
    - When middle == upper, our process is done.
    """
    pivot = A[i]
    lower, middle, upper = 0, 0, len(A)
    while middle < upper:
        if A[middle] < pivot:
            A[middle], A[lower] = A[lower], A[middle]
            lower, middle = lower + 1, middle + 1
        elif A[middle] == pivot:
            middle += 1
        else:
            upper -= 1
            A[middle], A[upper] = A[upper], A[middle]
