"""
Implement an algorithm that takes as input an array of distinct element and a size, and 
returns a subset of the given size of the array elements. All subsets should be equally
likely. Return the result in input array itself.

Let the input array be A, its length n, and specified size k. We build the random subset
using induction: to build a random subset of size exactly k, we first build one of size
k-1, then add one more element, selected randomly from the rest. 

Base case: k=1. We make one call to the random number generator, take the return value 
mod n (call it r), then swap A[0] with A[r]. Now A[0] holds the result.

Induction: for k > 1, we begin by choosing one element at random as above and now repeat
the same process with the n-1 element subarray A[1, n-1]. Eventually, the random subset
occupies A[0, k-1] and the remaining elements are in the last n-k slots.
"""
import random
def random_sampling(k, A):
    for i in range(k):
        # generate a random index in [i, len(A)-1].
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
