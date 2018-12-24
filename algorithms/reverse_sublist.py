class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

    def print_node(self):
        print('<{}>'.format(self.data), end='')
        if self.next:
            self.next.print_node()
        self:
            print()


def reverse_sublist(L, start, finish):
    """ Reverse the order of the nodes in L from start to finish, inclusive.
    
    Remarks.
    - The numbering of nodes starts at 1, i.e., 1st node refers to the head.

    Steps.
    1. First, we walk (start - 1) steps to reach the node before the sublist
       we want to reverse.

       L = [1, 2, 3, 4, 5, 6, 7, 8], start = 4

       dummy_head: ListNode(0., L); dummy_head.next points to 1
       sublist_head starts at dummy_head, then walks 4 - 1 = 3 steps:
          (0., ListNode(1, ...)) 
       -> (1, ListNode(2, ...)) First step
       -> (2, ListNode(3, ...)) Second step
       -> (3, ListNode(4, ...)) Third step
       
       sublist_iter      = sublist_head.next

       When this step finishes, we have:
       - dummy_head.next points to real head
       - sublist_head.next, aka. sublist_iter points to head of the subarray
       
    2. Next, we iteratively swap nodes.
        
                      sublist_iter
                            v
       0 -> [1,   2,   3,   4,   5,   6,   7,   8], start = 4
       ^               ^         
     dummy       sublist_head
        
       > temp              = sublist_iter.next

                   sublist_iter
                            v
       0 -> [1,   2,   3,   4,   5,   6,   7,   8], start = 4
       ^               ^         ^ 
     dummy       sublist_head   temp
    
       > sublist_iter.next = temp.next

                   sublist_iter ------.
                            v         V
       0 -> [1,   2,   3,   4,   5,   6,   7,   8], start = 4
       ^               ^         ^ 
     dummy       sublist_head   temp
    
       > temp.next         = sublist_head.next

                   sublist_iter --------,
                            v           v
       0 -> [1,   2,   3,   4, <-- 5,   6,   7,   8], start = 4
       ^               ^           ^ 
     dummy       sublist_head     temp
    

       > sublist_head.next = temp

                   sublist_iter --------,
                            v           v
       0 -> [1,   2,   3,   4, <-- 5,   6,   7,   8], start = 4
       ^               ^           ^ 
     dummy       sublist_head --> temp
    
    
       After this iteration, from the dummy_head's POV, we have:

                      sublist_head  sublist_iter
                            v             v
       0  ->  1  ->  2  ->  3  ->  5  ->  4  ->  6  ->  7  ->  8
       ^                           ^             ^     
     dummy                     prev_temp     next_temp


      Similarly, for next iteration:

                       sublist_head  sublist_iter ------,
                            v             v             v
       0  ->  1  ->  2  ->  3  ->  5  ->  4  ->  6  ->  7  ->  8
       ^                    |      ^             ^
     dummy                  |      '----------- temp
                            |                    ^
                            '--------------------'
      
      After next iteration:
          
                      sublist_head         sublist_iter
                           v                    v      
      0  ->  1  ->  2  ->  3  ->  6  ->  5  ->  4  ->  7  ->  8
      ^                           ^                    ^
    dummy                      prev_temp           next_temp


     Invariants:
     1. sublist_iter always points to the original head of the sublist, in this case, 4.
     2. temp is initialized to sublist_iter.next and will be moved to the head place of the 
        sublist.
     
     Swap:
     1. temp = sublist_iter.next: we want to move sublist_iter.next to the front of the 
        sublist.
     2. sublist_iter.next = temp.next: since temp will be gone soon (moved to the front),
        sublist_iter.next will point to the next node after temp.
     3. temp.next = sublist_head.next & sublist_head.next = temp: this is same as inserting 
        temp after sublist_head.

     Time complexity: O(f), where f is finish
    """

    dummy_head = sublist_head = ListNode(0., L)
    for _ in range(1, start):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp              = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next         = sublist_head.next
        sublist_head.next = temp

    return dummy_head.next





