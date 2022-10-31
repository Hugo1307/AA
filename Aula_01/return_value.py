## Crescimento quadrático: (n*(n+1))/2
 
def f1(n):

    r = 0
    iter_count = 0
    
    for i in range(1,n+1):
        r += i
        iter_count += 1
    
    return r, iter_count

sum, iter_count = f1(4)

print("Results for F1")
print()
print("Iterations Count: ", iter_count)
print("Sum: ", sum)

def r4(n): 

    if n == 0:
        return 0
    return 1 + r4(n-1) + r4(n-1)

print(r4(20))

def r2(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + r2(n-1)

print(r2(5))