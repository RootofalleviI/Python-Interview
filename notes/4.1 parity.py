def parity_brute_force(x):
    """
    The brute-force algorithm iteratively tests the value of each bit 
    while tracking the number of 1s seen so far. 

    Time: O(n) where n is the word size.
    """
    result = 0
    while x:
        print("result: {}, x: {}".format(result, x))
        result ^= 1
        x &= x - 1
    return result


def parity_erasing_lowest_one(x):
    """
    Improving the best-case and average-case performance by erasing the 
    lowest set bit in a word.

    Time: O(k) where k is the number of 1's.
    """
    result = 0
    while x:
        result ^= 1
        x &= x - 1 # drop the lowest set bit of x
    return result


def parity_caching(x):
    """
    Maintain a lookup table of 16-bit words and corresponding parity.
    First group: shifting right 3 * 16 = 48 bits => 16 leftmost bits left.
    Second group: shifting right 2 * 16 = 32 bits, then apply BIT_MASK to
        erase [16:31] bits and keep [0:15] for look up.
    Third group: shifting right 16 bits and apply similar MASK operation.
    Fourth group: apply mask directly to keep only the rightmost 16 bits.

    Time: O(n/L), where n is the word size and L be the subword size.
        In our case, n = 64 and L = 16.
    Space: O(2**L)
    """
    MASK_SIZE = 16
    BIT_MASK = 0b0000000000000011
    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
            PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
            PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK] ^
            PRECOMPUTED_PARITY[x & BIT_MASK])


def parity_XOR(x):
    """
    Since XOR is associative and commutative, we can split the 64-bit word
    to two 32-bit values A and B and compute A ^ B. This only takes a single
    right shift and a single 32-bit XOR instruction. We repeat the same  
    operation on 32-, 16-, 8-, 4-, 2-, and 1-bit operands to get the final
    results.

    As an example, we can calculate the parity of 11010111 in the following way:
    1. 00001101 XOR 11010111 => 11011010, we only care about the last 4 bits: 1010
        Shifting right 4 bits to obtain the left operand 00001101, then XOR it with
        the original 11010111 to obtain 11011010. Note that we only care about the
        right-most 4 bits.
   
    2. 00110110 XOR 11011010 => 11101100, we only care about the last 2 bits: 00
        We update x to be the result from last time. Then we shift x two bits to
        the right to obtain the left operand. Note that left[0-1] and right[0-1]
        are results from last time. Performing XOR on them and keep 2 non-significant
        bits to get us the next result.
        
    3. 01110110 XOR 11101100 => 10011010, we only care about the last 1 bit: 0
        Finally, we assign x to be the last result. We then initialize the left operand
        that equals x >> 1. The right-most bit of the result from this time is the parity.

    4. To extract the result, we apply bit-wise AND on result with 00000001.

    Time: O(log n), where n is the word size. 
    """
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0b1


# Exercise
# Write expressions that use bitwise operators, equality checks, and Boolean operators
# to do the following in O(1) time.

def propagate_rightmost_set_bit(x):
    """
    Right propagate the rightmost set bit in x, e.g., turns (01010000) to (01011111)
    """
    return x | (x-1)


def mod_2(x, y):
    """
    Compute x mode a power of two, e.g., returns 13 for 77 mod 64

    1. Propagate rightmost set bit for y.
    2. Turn off the leftmost set bit for y.
    3. Perform bit-wise AND
    """
    y = propagate_rightmost_set_bit(y)
    y >>= 1
    return x & y

def power_of_2(x):
    """
    Check if x is a power of 2, e.g., return True if x = 1, 2, 4, 8, ...
    """
    return 0 == x & (x-1)
