from functools import reduce
from string import hexdigits

def convert_base(num_as_string, b1, b2):
    """ Convert a number represented by a string from base b1 to base b2.

    :params num_as_string: string, representing an integer. '-' and 'A'~'F' are allowed.
    :params b1: source base
    :params b2: target base

    Example: num_as_string = 615, b1 = 7, b2 = 13
    - Convert 615 from base 7 to base 10.
        - 6 * 7 * 7 + 1 * 7 + 5 = (((6 * 7) + 1) * 7) + 5
        - Start from left with acc init to 0. 
        - Add the first digit, multiply it by 7 then add next digit.
        - Multiply the accumulator by 7 again then add next digit.
        - Until We run out of number.
    - Convert the intermediate result to base 13.
        - See construct_from_base
    """

    def construct_from_base(num_as_int, base):
        """ Convert an integer in base 10 to a target base.

        :params num_as_int: integer, in base 10.
        :params base: integer, the target base to convert to.

        Example: num_as_int = 306, base = 13. 
        - First digit: 306 % 13 = 7,
        - Update dividend: 306 / 13 = 23
        - Second digit: 23 % 13 = 10 => 'A',
        - Update dividend: 23 / 13 = 1,
        - Third digit: 1 % 13 = 1,
        - Update dividend: 1 / 13 = 0, END.

        Solution: 
        - Use mod to compute digit
        - Use div to update number
        - Terminate condition: number == 0
        """
        return ('' if num_as_int == 0 else
                construct_from_base(num_as_int // base, base) +
                hexdigits[num_as_int % base].upper())

    is_negative = num_as_string[0] == '-'
    num_as_int = reduce(
            lambda acc, x: acc * b1 + hexdigits.index(x.lower()),
            num_as_string[is_negative:], 0)

    sign = '-' if is_negative else ''
    if num_as_int == 0:
        return 0
    else:
        return construct_from_base(num_as_int, b2)

    
