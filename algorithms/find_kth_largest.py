# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3 and find_kth_largest(3, A) returns 1.

import random

def find_kth_largest(k, A):
    """ Given an array, find the kth largest element. 

    Strategy: select a pivot and partition the remaining entries into two groups.
    If there are exactly k-1 elements greater than the pivot, the pivot must be the kth largest 
    element; if there are more than k-1 elements greater than the pivot, we can discard elements
    less than or equal to the pivot as the kth largest element must be greater than the pivot; if
    there are less than k-1 elements greater than the pivot, we can discard elements greater than
    or equal to the pivot.

    O(n) average time with O(n^2) worst case time; O(1) space. """

    def find_kth(comp):
        """ Partition A[left:right + 1] around pivot_idx; return the new index of the pivot, 
        new_pivot_idx, after partition. After partitioning, A[left:new_pivot_index] contains
        elements that are greater than the pivot and A[new_pivot_idx + 1: right + 1] contains
        elements that are less than the pivot. """

        def partition_around_pivot(left, right, pivot_idx):
            pivot_value = A[pivot_idx]
            new_pivot_idx = left
            A[pivot_idx], A[right] = A[right], A[pivot_idx]
            for i in range(left, right):
                if comp(A[i], pivot_value):
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                    new_pivot_idx += 1
            A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]
            return new_pivot_idx

        left, right = 0, len(A) - 1
        while left <= right:
            pivot_idx = random.randint(left, right)
            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
            if new_pivot_idxd == k - 1:
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:
                left = new_pivot_idx + 1

    return find_kth(operator.gt)

find_kth_largest(2, [1, 3, 2, 4, 5, 7])
