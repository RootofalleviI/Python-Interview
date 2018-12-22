"""
Write a program which takes an integer and returns the inter
corresponding to the digits of the input written in reverse
order. For example, 42 => 24, -314 => -413.

Brute-Force.
Convert the input to a string, and then compute the reverse
from the string by traversing it from back to front. 

Mod-10.
The first digit can be obtained by taking the input mod 10.
Keep doing this and you will get the reversed number.

Time.
O(n), where n is the number of digits in k.
"""

def reverse(x):
    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        x_remaining //= 10
    return -result if x < 0 else result
