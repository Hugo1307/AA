calls = 0

def tribonacci(n):

    global calls

    if n <= 2:
        return n
    elif n == 3:
        return 4

    calls += 2
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

print(tribonacci(30))
print(calls) 