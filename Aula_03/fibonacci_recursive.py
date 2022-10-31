# Fibonacci Divide-And-Conquer
#
# Divide o problema em 2 - chama a função para n-1 e para n-2 
#
# Nº de Adições: Ai = 1 + Ai-1 + Ai-2

calls = 0

def fibonacci(n):
    
    global calls

    if n <= 1:
        return n
    
    calls += 1
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(1,20):
    print()
    print("N = ", i)
    print("Fn = ", fibonacci(i))
    print("An = ", calls)
    calls = 0