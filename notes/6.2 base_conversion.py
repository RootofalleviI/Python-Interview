"""
Write a program that performs base conversion. The input is a string, an integer b_1, and another
integer b_2. The string represents an integer in base b_1. The output should be the string 
representing the integer in base b_2. Assume 2 <= b_1, b_2 <= 16. 

Use A to represent 10, B for 11, etc. and F for 16.

Solution. We convert a string in base b_1 to integer type using a sequence of multiply and
adds. Then we convert that integer type to a string in base b_2 using a sequence of mod and divs.

Example. str = "615", b_1 = 7, b_2 = 13.
Then expressed in decimal, str has value 306. The least significant digit of the result is 
306 mod 13 = 7, then 306 / 13 = 23. Next digit is 23 mod 13 = 10, which is 1, then
23 / 13 = 1. Since 1 mod 13 = 1 and 1/13 = 0, the final digit is 1.
"""
import functools
def convert_base(num_as_string, b1, b2):
    def construct_from_base(num_as_int, base):
        return ('' if num_as_int == 0 else
                construct_from_base(num_as_int // base, base) +
                string.hexdigits[num_as_int % base].upper())

    is_negative = num_as_string[0] == '-'
    num_as_int = functools.reduce(
            lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
            num_as_string[is_negative:], 0)

    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else construct_from_base(num_as_int, b2))

