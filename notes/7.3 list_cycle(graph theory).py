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

    # None appears => list has an end => no cycle
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            print(slow.data, fast.data)
            # set cycle_len_advanced_iter to head
            cycle_len_advanced_iter = head
            
            print(cycle_len(slow))
            # advance cycle_len_advanced_iter to the current point of slow
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter = cycle_len_advanced_iter.next

            print(cycle_len_advanced_iter.data)
            # both iterator advance in tandom
            it = head
            while it is not cycle_len_advanced_iter:
                print("it: {} cycle: {}".format(it.data, cycle_len_advanced_iter.data))
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
                
            print("it: {} cycle: {}".format(it.data, cycle.data))

            return it # iter is the start of the cycle

    return None # No cycle


class Node:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node
        self.printed = 0
    def print_node(self):
        self.printed += 1
        print('<{}>'.format(self.data), end='')
        if self.next and not self.next.printed > 1:
            self.next.print_node()
        else:
            print()


A = Node(0, Node(1, Node(2, Node(3, None))))
cycle = Node(4, None)
B = Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, None))))))
A.next.next.next.next = cycle
cycle.next = B
B.next.next.next.next.next.next = cycle

A.print_node()
print(has_cycle(A).data)






