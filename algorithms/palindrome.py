def is_palindrome(s):
    """Test whether a string is a palindrome
    
    For simplicity, we define a palindrome string to be a string which when all the 
    non-alphanumerics are removed, it reads the same front to back ignoring case.
    
    The key is to use two pointers (indices).

    Time: O(n)
    """
    left, right = 0, len(s) - 1
    while left < right:
        while not s[left].isalnum() and left < right:
            left += 1
        while not s[right].isalnum() and left < right:
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left, right = left + 1, right - 1
    return True
