def can_form_palindrome(s):
    """ Given a string s, determine whether the letters from s can be permuted to 
    form a palindrome.

    @Stratety: if the string is of even length, a necessary and sufficient condition
    for it to be a palindrome is that each character in the string appears an even
    number of times. If the length is odd, all but one character should appear an
    even number of times. 

    O(n) time, where n is the length of the string;
    O(c) space, where c is the number of distinct characters.
    """

    return sum(v % 2 for v in collections.Counter(s).values()) <= 1
