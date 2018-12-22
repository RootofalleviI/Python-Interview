"""
Write a program that takes a double x and an integer y and returns x^y.
Ignore overflow and underflow.

Solution.
- The brute-force way is to multiple x by itself y times.
- The key to efficiency is to get more work done with each multiplication.
- For example, x^{10} = x^{5+5} = x^{5} * x^{5} and x^{5} = x * x^{2} * x^{2}.
- Genralizing, if LSB of y is 0, the result is (x^{y/2})^2; otherwise, it is
x * (x^{y/2})^2. This gives us a recursive algorithm for computing x^y when
y is non-negative. 
- When y is negative, we replace x by 1/x and y by -y.
- We replace the recursion with a while loop to avoid the overhead of function calls.

Time: The number of multiplications is at most twice the index of y's MSE, implying an
O(n) time complexity.
"""

def power(x, y):
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x
    while power:
        print("x={}, power={}, result={}".format(x, power, result))
        if power & 1:       
            result *= x     
        x, power = x * x, power >> 1
    return result
