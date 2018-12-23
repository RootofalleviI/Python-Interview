"""
Write a program that takes an array and reorders its entries so that the
even entries appear first. Do not allocate extra space.

We partition the array into three subarrays: Even, Unclassified, and Odd, 
appearing in that order. Initially Even and Odd are empty, and Unclassified
is the entire array. We iterate through Unclassified, moving its elements to
the boundaries of the Even and Odd subarrays via swaps, thereby expanding
Even and Odd, and shrinking Unclassified.

O(n) time, O(1) space.
"""

def even_odd(A):
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

