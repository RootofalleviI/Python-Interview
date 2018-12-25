def is_letter_constructible_from_magazine(letter_text, magazine_text):
    """ Given text for a letter and text from a magazine, determine if it is
    possible to write the anonymous letter using the magazine. More precisely,
    the letter can be written if for each character in the anonymous letter, 
    the number of times it appears in the anonymous letter is no more than the
    number of times it appears in the magazine.

    Time: O(m+n), where m, n represent number of characters in text and magazine.
    Space: O(L), where L is the number of distinct characters appearing in the letter.
    """

    # Document how many characters we need for the letter
    char_frequency_for_letter = collections.Counter(letter_text)

    # Loop through the magazine text
    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -= 1
            if char_frequency_for_letter[c] == 0:
                del char_frequency_for_letter[c]
                if not char_frequency_for_letter:
                    return True

    # If all characters are covered, return True.
    return not char_frequency_for_letter
