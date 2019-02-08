def groupBy4(A, doc):
    b0, b1, b2, b3 = 0, 0, 0, len(A)
    while b2 < b3: # k-2 < k-1
        if (A[b2] == doc[3]): # k-1
            b3 -= 1
            A[b2], A[b3] = A[b3], A[b2]
        elif (A[b2] == doc[2]): # k-2
            b2 += 1
        elif (A[b2] == doc[1]): # k-3 = 1
            A[b2], A[b1] = A[b1], A[b2]
            b1, b2 = b1+1, b2+1
        else: # k-4 = 0
            A[b2], A[b1] = A[b1], A[b2]
            A[b1], A[b0] = A[b0], A[b1]
            b0, b1, b2 = b0+1, b1+1, b2+1

n = len(A)
k = 3
def whichPart(n):
    return n % k

def groupByk(A, n, k):
    ptrs = {}
    for i in range(0, k-1):
        ptrs[i] = 0
    ptrs[k-1] = n
    while ptrs[k-2] < ptrs[k-1]:
        partition = whichPart(A[ptrs[k-2]])
        print(f"pointer: {ptrs[k-2]}")
        print(f"number: {A[ptrs[k-2]]}, partition: {partition}")
        if partition == k-1:
            ptrs[k-1] -= 1
            A[ptrs[k-2]], A[ptrs[k-1]] = A[ptrs[k-1]], A[ptrs[k-2]]
        elif partition == k-2:
            ptrs[k-2] += 1
        else:
            for i in range(k-2, partition, -1):
                print(f"swapping: {A[ptrs[i]]}, {A[ptrs[i-1]]}")
                A[ptrs[i]], A[ptrs[i-1]] = A[ptrs[i-1]], A[ptrs[i]]
            for i in range(partition, k-1):
                print(f"incrementing: {i}")
                ptrs[i] += 1
        print(A)
        print(ptrs)
        print('='*20)

groupByk(A, n, k)
print(A)
