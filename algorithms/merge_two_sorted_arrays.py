def merge_two_sorted_arrays(A, m, B, n):
    """ Given two sorted array A with length m and B with length n, merge them and write the result
    to array A. 

    We start from the back:
    A = [5, 13, 17, None, None, None, None, None]
    B = [3, 7, 11, 19]

    Then
    A = [5, 13, 17, None, None, None, 19, None]
    A = [5, 13, 17, None, None, 17, 19, None]
    A = [5, 13, 17, None, 13, 17, 19, None]
    A = [5, 13, 17, 11, 13, 17, 19, None]   
    A = [5, 13, 7, 11, 13, 17, 19, None]  
    A = [5, 5, 7, 11, 13, 17, 19, None]  
    A = [3, 5, 7, 11, 13, 17, 19, None]  

    Time: O(m + n), Space O(1) """

    a, b, write_idx = m - 1, n - 1, m + n - 1
    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[write_idx] = A[a]
            a -= 1
        else:
            A[write_idx] = B[b]
            b -= 1
        write_idx -= 1
    while b >= 0:
        A[write_idx] = B[b]
        write_idx, b = write_idx - 1, b - 1
