def group_by(A, doc):
    """ Assuming that keys take one of four values, reorder the array so that 
    all objects with the same key appear together. The order of subarrays is 
    not important. 

    :params A: list, the array for reordering
    :params doc: list, containing unique values of A (thus has length 4)

    Time complexity: O(n)
    Space complexity: O(1)

    We use the same approach as in partition, i.e., keep a few partition flags
    denoting boundaries of subarrays. While we loop over each element in the
    array, we do adequate element swaps and flag shifts.

    Invariants:
    - A[:b1]: containing A's
    - A[b1:b2]: containing B's
    - A[b2:b3]: containing C's
    - A[b3:b4]: unclassified
    - A[b4:]: containing D's

    Extra remark:
    - A[b3] is the element currently processing.

    We handle group D and group C the same way we handled the middle and left 
    groups in partition algorithm. For group A and B it gets a bit more complex:
    if the element is a B, we need to swap it with A[b2] and increment both b2 & b3;
    if the element is an A, we need to first swap it with A[b2], then swap A[b2] with
    A[b3], finally we increment b1, b2 and b3.
    """
    b1, b2, b3, b4 = 0, 0, 0, len(A)
    while b3 < b4:
        if (A[b3] == doc[3]):
            b4 -= 1
            A[b3], A[b4] = A[b4], A[b3]
        elif (A[b3] == doc[2]):
            b3 += 1
        elif (A[b3] == doc[1]):
            A[b3], A[b2] = A[b2], A[b3]
            b2, b3 = b2+1, b3+1
        else:
            A[b3], A[b2] = A[b2], A[b3]
            A[b1], A[b2] = A[b2], A[b1]
            b1, b2, b3 = b1+1, b2+1, b3+1

