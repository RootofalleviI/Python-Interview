def reverse_words(s):
    """ Given a string containing a set of words separated by whitespaces, we would like
    to transform it to a string in which the words appear in the reverse order. We do not
    need to keep the original string. 

    Strategy:
    - Reversing s gets the words to their correct relative positions, but in reversed order.
    - Reversing individual words turns the string into the correct form.

    Example: 
    - ram is costly => yltsoc si mar => costly is ram
    
    Time: O(n).
    Space: O(1).
    """
    
    def reverse_range(s, start, end):
        """ Reversing an individual word """
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end + 1

    start = 0
    while True:
        end = s.find(b' ', start)
        if end < 0:
            break 

        # Reverse each word in the string
        reverse_range(s, start, end - 1)
        start = end + 1

    # Reverse the last word
    reverse_range(s, start, len(s) - 1)

