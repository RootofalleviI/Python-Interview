def remove_kth_last(L, k):
    """ Assume L has at least k nodes, delete the k-th last node in L.
    
    We use two iterators. The first iterator is advanced by k steps, and then
    the two iterators advance in tandem. When the first iterator reaches the tail,
    the second iterator is at the (k+1)th last node. We can then remove thekth node.

    Example. L = [0, 1, 2, 3, 4, 5], k = 2, i.e., remove <4>.

    First, we advance pointer 1 two steps:
        
    [0, 1, 2, 3, 4, 5]
     ^
   first

    > for _ in range(k): first = first.next

    [0, 1, 2, 3, 4, 5]
           ^
         first

    > second = dummy_head

   second
     v
    [0, 1, 2, 3, 4, 5]
           ^
         first

    > while first: first, second = first.next, second.next

            second
              v
    [0, 1, 2, 3, 4, 5]
                    ^
                  first

            second
              v
    [0, 1, 2, 3, 4, 5] x
                       ^
                     first

            second -,
              v     v
    [0, 1, 2, 3, 4, 5]  => [0, 1, 2, 3, 5]
                 ^
            second.next

    """           

    dummy_head = ListNode(0, L)
    first = dummy_head.next
    for _ in range(k):
        first = first.next

    second = dummy_head
    while first:
        first, second = first.next, second.next
    second.next = second.next.next
    
    return dummy_head.next
