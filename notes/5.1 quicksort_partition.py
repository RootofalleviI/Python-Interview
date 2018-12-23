"""
Write a program that takes an array A and an index i into A, and rearranges the
elements such that all elements less than A[i], the pivot, appears first, followed
by elements equal to the pivot, followed by elements greater than the pivot.

Trivial: Using O(n) space with O(n) time.

Improvement: Avoid O(n) space at the cost of increased time complexity.
"""

RED, WHITE, BLUE = range(3)

def dutch_flag_partition_one(pivot_index, A):
    """
    Time: O(n^2)
    Space: O(1)
    """
    pivot = A[pivot_index]
    print("Before:", A)
    print("Pivot:", pivot)
    
    # First pass: group elements small than pivot
    print("="*20)
    print("First pass:")
    for i in range(len(A)):
        print("i:", i)
        print("Current:", A)

        # Look for a smaller element.
        for j in range(i + 1, len(A)):
            print("j:", j)
            print("Comparing A[{}]={} with pivot={}".format(j, A[j], pivot))
            if A[j] < pivot:
                print("A[{}]={} < pivot={}. Switch {} with {}".format(j, A[j], pivot, A[i], A[j]))
                A[i], A[j] = A[j], A[i]
                break
            else:
                print("A[{}]={} >= pivot={}. Continue".format(j, A[j], pivot))
                

    print("="*20)
    print("Second pass:")
    # Second pass: group elements larger than pivot
    for i in reversed(range(len(A))):
        print("i:", i)
        print("Current:", A)
        if A[i] < pivot:
            break

        # Look for a larger element. Stop when we reach an element 
        # less than pivot, since first pass has moved them to the 
        # start of A.
        for j in reversed(range(i)):
            print("j:", j)
            if A[j] > pivot:
                print("A[{}]={} > pivot={}. Switch {} with {}".format(j, A[j], pivot, A[i], A[j]))
                A[i], A[j] = A[j], A[i]
                break
            else:
                print("A[{}]={} >= pivot={}. Continue".format(j, A[j], pivot))
    
    print("After:", A)


def dutch_flag_partition_two(pivot_index, A):
    """
	Time: O(n)
	Space: O(1)
    """
    pivot = A[pivot_index]
    print("Before:", A)
    print("Pivot:", pivot)
    
    # First pass: group elements small than pivot
    print("="*20)
    print("First pass:")
    smaller = 0
    for i in range(len(A)):
        print("i: {}, smaller: {}".format(i, smaller))
        print("Current:", A)
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
                

    print("="*20)
    print("Second pass:")
    # Second pass: group elements larger than pivot
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        print("i: {}, larger: {}".format(i, larger))
        print("Current:", A)
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1
    print("After:", A)


def dutch_flag_partition(pivot_index, A):
    """
    O(n) time and O(1) space
    """
    pivot = A[pivot_index]

    # Invariants:
    # bottom group: A[:smaller]
    # middle group: A[smaller:equal]
    # unclassified: A[equal:larger]
    # top group: A[larger:]

    smaller, equal, larger = 0, 0, len(A)
    
    # Keep iterating as long as there is an unclassified element.
    while equal < larger:
        print("==" * 20)
        print("smaller: {}, equal: {}, larger: {}".format(smaller, equal, larger))
        print("Currently classifying {}".format(A[equal]))
        print("bottom group", A[:smaller])
        print("middle group", A[smaller:equal])
        print("unclassified", A[equal:larger])
        print("top group", A[larger:])
        print("overall", A)

        # A[equal] is the incoming unclassified element
        if A[equal] < pivot:
            print("A[equal] < pivot, put into bottom group")
            A[smaller], A[equal] = A[equal], A[smaller]
            print("Increment smaller and equal")
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            print("A[equal] == pivot")
            print("Increment equal")
            equal += 1
        else: # A[equal] > pivot
            print("A[equal] > pivot")
            larger -= 1
            print("Decrementing larger, put into top group")
            A[equal], A[larger] = A[larger], A[equal]

dutch_flag_partition(2, [1, 4, 2, 8, 5, 2, 8, 7])
