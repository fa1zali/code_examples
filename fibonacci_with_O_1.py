# Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))