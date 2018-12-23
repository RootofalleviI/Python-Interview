def count_bits(x):
    """Count the number of bits that are set to 1 in a positive integer
    
    :param x: positive integer
    :return: the number of bits that are set to 1 when x is converted to binary

    Technical notes:
    1. Bitwise and, i.e. (x & y): convert x and y to binary, perform bit-wise and,
       then convert the result back to decimal. 
       
       Example: (60 & 13) => 12
       - bin(60) = 0011 1100
       - bin(13) = 0000 1101
       - 60 & 13 = 0000 1100
       - decimal = 8 + 4 = 12

    2. Bitwise right shift, i.e., x >>= 1: convert x to binary, shift everything to
       the right, then convert it back. Essentially does an integer divide by 2.

       Example: 60 >> 1 => 30
       Example: 61 >> 1 => 30

    Complexity:
    1. Time - 1 bitwise and takes O(1); 1 bitwise shift takes O(1); we are doing it
       n times (where n represents the length of x represented in binary), the overall
       time complexity if O(n).
    2. Space - We are not storing anything so it's O(1).
    """

    num_bits = 0
    while x:
        print("Current number:", x)
        num_bits += x & 1
        x >>= 1
    return "Result:", num_bits
