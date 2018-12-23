""" 
Write a program that takes an integer and determine if that integer's
representation as a decimal string is a palindrome.

Remark. If the input is negative, its string representation starts with
a negative sign -, thus it cannot be a palindrome.

Brute-force.
Convert the input to a string, iterate through the string, do pairwise
comparison on LSB and MSB, working inwards until there is a mismatch.
Time and space complexity: O(n), where n is the number of digits in the input.

Avoid O(n) space.
- The number of digits, n, equals log_10(x), i.e., n = math.floor(log10(x)) + 1.
- Least significant digit: x mod 10
- Most significant digit: x/(10^{n-1})
- Keep removing them from the original number.

Result: Time O(n), space O(1).

Alternatively, we can use the reverse algorithm with O(n) time and see if it is
unchanged.
"""

def is_palindrome_number(x):
    if x <= 0:
        return x == 0
    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10 ** (num_digits - 1)
    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask # remove the most significant digit of x
        x //= 10      # remove the least significant digit of x
        msd_mask //= 100
    return True

