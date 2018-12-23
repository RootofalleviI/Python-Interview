"""
Write a program that takes two arrays representing integers, and returns an array representing
an integer which is their product. 

Example: 123 * 987 = 7 * 123 + 8 * 123 * 10 + 9 * 123 * 100
Representation: 1934 => <1, 9, 3, 4>; -7094 => <-7, 0, 9, 4>

There are m partial products, each with at most n+1 digits. We perform O(1) operation on each
digit in each partial product, so the time complexity is O(mn).
"""

def multiply(num1, num2):
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    result = [0] * (len(num1) + len(num2))

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    for i in range(len(result)):
        if result[i] != 0:
            result = result[i:]
            break
            
    return [sign * result[0]] + result[1:]

