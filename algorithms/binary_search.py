def bsearch(t, A):
    """ A binary search implementation. """
    L, U = 0, len(A) - 1
    while L <= U:
        M = L + (U - L) // 2    # preventing overflow
        if A[M] < t:
            L = M + 1
        elif A[M] == t:
            return M
        else:
            U = M - 1
    return -1


# To find the first element that is not less than a target value, use `bisect.bisect_left(a, x)`.
# This call returns the index of the first entry that is greater than or equal to the targeted value.
# If all elements in the list are less than x, the returned value is len(a).

# To find the first element that is greater than a target value, use `bisect.bisect_right(a, x)`.
# This call returns the index of the first entry that is greater than the targetd value.
# If all elements in the list are less than or equal to x, the returned value is len(a).

def search_first_of_k(A, k):
    """ Return the index of first occurrence of k in array A. O(log n) """
    left, right, result = 0, len(A) - 1, -1

    # Invariant: A[left: right+1] is the candidate set.
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1 # Nothing to the right of mid can be solution
        else:
            left = mid + 1

    return result
    

def search_first_greater_than_k(A, k):
    """ Return the index of the first element that is greater than k.
    O(log n).
    """

    left, right, result = 0, len(A) - 1, -1
    
    # Invariant: A[left:] is the candidate set.
    while left <= right:
        mid = (left + right) // 2
        print("left={}, right={}, mid={}".format(left, right, mid))
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            left = mid + 1
            result = left
        else:
            left = mid + 1

    return result


def cyclic_search(A):
    """ Find the position of the smallest element in a cyclically sorted array.
    Assume all elements are distinct. O(log n). """

    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[right]:
            # Minimum must be in A[mid+1:right+1]
            left = mid + 1
        else:
            # Minimum must be in A[left:mid+1]
            right = mid

    # Loop ends when left == right
    return left


def integer_square_root(k):
    """ Compute math.floor(math.sqrt(k)) """
    left, right = 0, l

    # Invariant: candidate integer [left, right]
    # Eerything before left has square <= k; everything after has square > k.
    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid
        if mid_squared <= k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1



