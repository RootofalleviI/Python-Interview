def groupBy(A, doc):
    lower, middle, upper = 0, 0, len(A)
    while middle < upper:
        if A[middle] == doc[0]:
            A[middle], A[lower] = A[lower], A[middle]
            lower, middle = lower+1, middle+1
        elif A[middle] == doc[1]:
            middle += 1
        else:
            upper -= 1
            A[middle], A[upper] = A[upper], A[middle]

def groupBy4(A, doc):
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

def groupByBool(A):
    b1, b2 = 0, 0
    while b2 < len(A):
        if A[b2]:
            b2 += 1
        else:
            A[b1], A[b2] = A[b2], A[b1]
            b1, b2 = b1+1, b2+1

A = [True, False, False, True, True, False]
groupByBool(A)
print(A)
