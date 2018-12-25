def find_nearest_repetition(paragraph):
    """ Given an input array, find the distance between a closest pair of equal entries.

    @Strategy: as we scan through the array, we store in a hashtable the latest index
    at which a word appears.

    Time O(n), Space O(d), where d is the number of distinct entries in the array. """
    word_to_latest_index, nearest_repeated_distance = {}, float('inf')
    for i, word in enumerate(paragraph):
        if word in word_to_latest_index:
            latest_equal_word = word_to_latest_index[word]
            nearest_repeated_distance = min(nearest_repeated_distance, i-latest_equal_word)
        word_to_latest_index[word] = i
    return nearest_repeated_distance if nearest_repeated_distance != float('inf') else -1
