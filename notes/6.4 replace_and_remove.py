"""
Write a program which takes as input an array of characters, removes each 'b' and replaces each
'a' by two 'd's. Specifically, along with the array, you are provided an integer-valued size, which
denotes the number of entries of the array that the operation is to be applied to. You do not have
to worry about preserving subsequence entries.

If there are no a's, we can implement the function without allocating additional space with one
forward iteration by skipping b's and copying over the other characters.

If there are no b's, we can implement the function without additional space as follows. First,
we compute the final length of the resulting string, which is the length of the array plus the
number of a's. We can then write the result, character by character, starting from the last char,
working our way backwards.

To combine them, we first delete b's and compute the final number of valid characters of the string,
with a forward iteration through the string. Then we replace each a's by two d's, iterating backwards
from the end of the resulting string.

"""

def replace_and_remove(size, s):
    write_idx, a_count = 0, 0
    for i in range(size):
        print("Current s:", s)
        print("write_idx={}, a_count={}".format(write_idx, a_count))
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1
        print("write_idx={}, a_count={}".format(write_idx, a_count))
    print('='*20)
    cur_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    while cur_idx >= 0:
        print("Current s:", s)
        print("cur_idx={}, write_idx={}".format(cur_idx, write_idx))
        if s[cur_idx] == 'a':
            s[write_idx - 1: write_idx + 1] = 'dd'
            write_idx -= 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        cur_idx -= 1
    return final_size

from random import choice
s = ['a', 'c', 'd', 'b', 'b', 'c', 'a']
# s = ['a', 'b'] * 4
# s = [choice(['a', 'b', 'c']) for i in range(20)]
replace_and_remove(7, s)
print(s)
