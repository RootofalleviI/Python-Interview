class Queue:
    """ A queue API using an array for storing elements with dynamic recizing.

    Dequeue: O(1)
    Enqueue: amortized O(1)

    > q = Queue(3)

                  tail
                   v
        entries: [None, None, None], num = 0
                   ^
                  head

    > q.enqueue(0)

                     tail
                      v
        entries: [0, None, None], num = 1
                  ^
                 head
    
    > q.enqueue(1)

                        tail
                         v
        entries: [0, 1, None], num = 2
                  ^
                 head

    > q.enqueue(2)

                 tail
                  v
        entries: [0, 1, 2], num = 3
                  ^
                 head

    > q.dequeue()

                 tail
                  v
        entries: [0, 1, 2], num = 2
                     ^
                    head

    > q.enqueue(4)

                    tail
                     v
        entries: [4, 1, 2], num = 3
                     ^
                    head

    > q.enqueue(5)

                              tail
                               v 
        entries: [1, 2, 4, 5, None, None], num = 4
                  ^
                 head


    Invariants:
    - head always points to the first element of the queue, i.e., the thing you return
      when dequeue() is called.
    - tail always points to the next available position for enqueuing; it's either a None
      or a number that has already been erased. 
    - Note that when a Queue is full, head = tail as next enqueuing triggers an resize.
    - Both head and tail update are calculated using `head = (head + 1) % len(entries)`.
    """

    SCALE_FACTOR = 2

    def __init__(self, capacity):
        self._entries = [None] * capacity
        self._head = self._tail = self._num_queue_elements = 0
        self.print_queue()

    def enqueue(self, x):
        if self._num_queue_elements == len(self._entries):
            self._entries = self._entries[self._head:] + self._entries[:self._head]
            self._head, self._tail = 0, self._num_queue_elements
            self._entries += [None] * (
                    len(self._entries) * Queue.SCALE_FACTOR - len(self._entries))

        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)
        self._num_queue_elements += 1
        self.print_queue()

    def dequeue(self):
        if not self._num_queue_elements:
            raise IndexError("Empty Queue")
        self._num_queue_elements -= 1
        ret = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
        self.print_queue()
        return ret

    def size(self):
        return self._num_queue_elements

    def print_queue(self):
        print("Current entries:", self._entries)
        print("Head: [{}]-{}, Tail: [{}]-{}".format(self._head, 
            self._entries[self._head], self._tail, self._entries[self._tail]))
