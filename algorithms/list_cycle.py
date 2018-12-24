def has_cycle(head):
    """ Given the head of a singly linked list, return null if there does not exist a 
    cycle, or the node at the start of the cycle if a cycle is present. The length of
    the list is not given in advance.

    We use two iterators to traverse the list. In each iteration, advance the slow 
    iterator by one and the fast iterator by two. The list has a cycle if and only if
    the two iterators meet.

    Time complexity: O(n)
    """

    def cycle_len(end):
        """ Detect the length of cycle """
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step

    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            cycle_len_advanced_iter = head
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter = cycle_len_advanced_iter.next

            it = head
            while it is not cycle_len_advanced_iter:
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
                
            return it # iter is the start of the cycle

    return None # No cycle


