def fib_memo(n):
    def helper(n):
        if memo[n] is not None:
            return memo[n]
        if n == 0:
            result = 0
        elif n == 1 or n == 2:
            result = 1
        else:
            result = helper(n-1) + helper(n-2)
        memo[n] = result
        return result
    
    memo = [None] * (n + 1)      
    return helper(n)


print(fib_memo(23))
