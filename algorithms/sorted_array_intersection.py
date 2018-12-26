def intersect_two_sorted_array(A, B):
    """ Given two sorted arrays A, B, return entries that present in both arrays. 

    Time: O(m+n), where m = len(A) and n = len(B).
    """
    i, j, intersection_A_B = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersection_A_B.append(A[i])
            i, j = i + 1, j + 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1

    return intersection_A_B
