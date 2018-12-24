class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node
    def print(self):
        print(self.data, end='')
        if self.next:
            self.next.print()
        else:
            print()

# O(n)
def search_list(L, key):
    while L and L.data != key:
        L = L.next
    return L


# O(1)
def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node


# O(1)
def delete_after(node):
    node.next = node.next.next


# Time O(n+m), Space O(1)
def merge_two_sorted_lists(L1, L2):
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2
    return dummy_head.next


# O(finish)
def reverse_single_sublist(L, start, finish):
    """ Reverse the order of the nodes from start to finish, inclusive. """
    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, start):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        print("Before:", end='')
        dummy_head.next.print()
        try: 
            print("sublist_head: {}->{}, sublist_iter: {}->{}, temp: {}->{}"
                .format(sublist_head.data, sublist_head.next.data,
                    sublist_iter.data, sublist_iter.next.data,
                    temp.data, temp.next.data))
        except Exception as e:
            print(e)
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp
        print("After:", end=''),
        dummy_head.next.print()
        try:
            print("sublist_head: {}->{}, sublist_iter: {}->{}, temp: {}->{}"
                .format(sublist_head.data, sublist_head.next.data,
                    sublist_iter.data, sublist_iter.next.data,
                    temp.data, temp.next.data))
        except Exception as e:
            print(e)
    return dummy_head.next


L = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))))
reverse_single_sublist(L, 2, 5)
