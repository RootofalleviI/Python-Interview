""" A heap is a specialized binary tree. Specifically, it is a complete binary tree whose keys must 
satisfy the "heap property" -- the key at each node is at least as great as the keys stored at its
children.

A max-heap can be implemented as an array; the children of the node at index i are at indices
2i+1 and 2i+2. A max-heap supports O(log n) insertions, O(1) time lookup for max element, and O(log n) 
deletion of the max element. The extract-max operation is defined to delete and return the maximum 
element. Searching for arbitrary keys takes O(n) time complexity.

A heap is sometimes referred to as a priority queue because it behaves like a queue, with one 
difference: each element has a "priority" associated with it, and delete removes the element with
the highest priority.

The min-heap is a completely symmetric version of the data structure and supports O(1) time lookups 
for the minimum element.

Use a heap when all you care about is the max or min element, and you do not need to support fast
lookup, delete, or search operations for arbitrary elements. To compute the k largest elments in a 
collection, use a min-heap; to compute the k smallest elements, use a max-heap.

Heap library: `heapq` module.
- `heapq.heapify(L)`: transforms elements in L into a heap in-place,
- `heapq.nlargest(k, L)` and `heapq.nsmallest(k, L)`: returns the k largest/smallest elements in L,
- `heapq.heappush(h, e)`: pushes a new element on the heap,
- `heapq.heappop(h)`: pops the smallest element from the heap,
- `heapq.heappushpop(h, a)`: pushes `a` on the heap then pops and returns the smallest element,
- `e = h[0]`: returns the smallest element on the heap without popping it.

It is important to remember that `heapq` only provides min-heap functionality. If you need to build
a max-heap on integers or floats, insert their negative to get the effect of a max-heap using `heapq`.
"""
