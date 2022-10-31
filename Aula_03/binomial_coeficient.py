def binomial_coeficient(n, j):

    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return binomial_coeficient(n-1, j) + binomial_coeficient(n-1, j-1)
    
print(binomial_coeficient(2,5))