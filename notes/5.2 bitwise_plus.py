"""
Write a program which takes as input an array of digits encoding a nonnegative 
decimal integer D and updates the array to represent the integer D+1. For example,
if the input is <1, 2, 9>, then you should update the array to <1, 3, 0>. Your 
algorithm should work even if it is implemented in a language that has finite-
precision arithmetic.

Time: O(n), where n is the length of A.
"""

def plus_one(A):
    A[-1] += 1                                  # increment
    for i in reversed(range(1, len(A))):
        if A[i] != 10:                          # no need to carry digit
            break
        A[i] = 0                                # otherwise, carry digit
        A[i - 1] += 1
    if A[0] == 10:                              # if first digit is 10
        A[0] = 1                                # set the first to 1
        A.append(0)                             # and append a 0 at the end


def binary_plus(x, y):
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    result = ''
    carry = 0

    for i in range(max_len-1, -1, -1):
        r = carry
        r += 1 if x[i] == '1' else 0
        r += 1 if y[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1

    if carry != 0:
        result = '1' + result

    return result.zfill(max_len)

print(binary_plus('11', '1'))
print(binary_plus('10', '10'))
print(binary_plus('111', '111'))
print(binary_plus('1111111', '1'))
