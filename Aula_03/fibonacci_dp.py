# Fibonacci With Dynamic Programming

cache = {}
calls = 0

def fibonacci(n):

    global cache, calls

    if n <= 1:
        return n

    if n-1 not in cache:
        cache[n-1] = fibonacci(n-1) 
    if n-2 not in cache:
        cache[n-2] = fibonacci(n-2)

    calls += 1

    return cache[n-1] + cache[n-2]


# Python Way From Slides
from functools import wraps

def memo (func):

    cache = {}

    @wraps(func)
    def wrap (*args): 
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


for i in range(1,20):

    print()
    print("N = ", i)
    print("Fn = ", fibonacci(i))
    print("An = ", calls)
    calls = 0

    # Without Memoization
    # Comment line below to use Memoization
    cache = {}
