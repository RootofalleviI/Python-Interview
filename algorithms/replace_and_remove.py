def replace_and_remove(size, s):
    """ Write a program which takes as input an array of characters and:
        1. removes each 'b'
        2. replace each 'a' with two 'd's.
    You only need to perform this operation on first `size` elements of s. 
    You do not need to worry about perserving subsequent entries and you 
    can assume there is enough space in the array to hold the final result.

    :params size: integer, number of elements you need to worry about.
    :params s: list of integers

    Example: [a, c, d, b, b, c, a]
    First pass: we delete b's by skipping it and compute the final number of valid characters of string.
    
       [a, c, d, b, b, c, a], write_cursor := 0, num_of_a := 0
    => [>a, c, d, b, b, c, a], write_cursor = 0, num_of_a = 0
        - s[0] <- s[0], write_cursor <- 1, num_of_a <- 1
    => [a, >c, d, b, b, c, a], write_cursor = 1, num_of_a = 1
        - s[1] <- s[1], write_cursor <- 2
    => [a, c, >d, b, b, c, a], write_cursor = 2, num_of_a = 1
        - s[2] <- s[2], write_cursor <- 3
    => [a, c, d, >b, b, c, a], write_cursor = 3, num_of_a = 1
        - no copying
    => [a, c, d, b, >b, c, a], write_cursor = 3, num_of_a = 1
        - no copying
    => [a, c, d, b->c, b, >c, a], write_cursor = 3, num_of_a = 1
        - s[3] <- s[5], write_cursor <- 4
    => [a, c, d, c, b->a, c, >a], write_cursor = 4, num_of_a = 1 
        - s[4] <- s[6], write_cursor <- 5, num_of_a <- 2
    => END of pass 1: [a, c, d, c, a, c, a], write_cursor = 5, num_of_a = 2

    source_cursor = write_cursor - 1 => 4 
    write_cursor += num_of_a - 1  => 6: we start from s[6] when we do the (backward) second pass. 
    final_size = write_cursor + 1 => 7: the length of result string will be 7.
    
    Second pass: we replace each a by two d's, iterating from back to front.

       [a, c, d, c, +a, c, *a], write_cursor(*) = 6, source_cursor(+) = 4
    => [a, c, d, +c, *a, c->d, a->d]
        - write_cursor <- 4, source_cursor <- 3
    => [a, c, +d, *c, a->c, d, d]
        - write_cursor <- 3, source_cursor <- 2
    => [a, +c, *d, c->d, c, d, d]
        - write_cursor <- 2, source_cursor <- 1
    => [+a, *c, d->c, d, c, d, d]
        - write_cursor <- 1, source_cursor <- 0
    => [a->d, c->d, c, d, c, d, d]
        - END
    => [d, d, c, d, c, d, d]
    """
    write_cursor, num_of_a = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[write_cursor] = s[i]
            write_cursor += 1
        if s[i] == 'a':
            num_of_a += 1

    source_cursor = write_cursor - 1
    write_cursor += num_of_a - 1
    final_size = write_cursor + 1
    while source_cursor >= 0:
        if s[source_cursor] == 'a':
            s[write_cursor - 1: write_cursor + 1] = 'dd'
            write_cursor -= 2
        else:
            s[write_cursor] = s[source_cursor]
            write_cursor -= 1
        source_cursor -= 1
    return final_size




