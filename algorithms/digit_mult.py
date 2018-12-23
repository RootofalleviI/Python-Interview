def multiply(num1, num2):
    """ Given two arrays representing two integers, return an array representing their product.

    :params num1: array of integers, first entry may be negative.
    :params num2: array of integers, first entry may be negative.

    Example: [-2, 0, 7, 4] represents integer -2074.

    Grade-school multiplication method.
    
    Time complexity: O(mn), where m = len(num1) and n = len(num2)

    Extra remarks.
    - result[i + j + 1] represents the digit directly below what we are processing.
    - result[i + j] represents the digit left to result[i + j + 1].
    - We first assign result[i + j + 1] the multiplication result, then update the carried digits
      to result[i + j]. Finally, we perform mod 10 on result[i + j + 1].
    """
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0], num2[0])
    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10
    for i in range(len(result)):
        if result[i] != 0:
            result = result[i:]
    return result





