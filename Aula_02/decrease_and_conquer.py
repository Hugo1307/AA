results = {}
counter = 0

def power(a, b):

    global results
    global counter

    counter += 1

    if b == 1:
        results[(a,b)] = 1
        return a
    
    p = power(a, b//2)

    if b%2 == 0:
        return p * p
    return a * p * p

print(power(2,7))
print(counter)