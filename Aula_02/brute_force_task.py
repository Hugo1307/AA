import sys

def power(a, b):

    total = a
    multiplications_count = 0

    for _ in range(1, b):
        total *= a
        multiplications_count += 1 
    return total, multiplications_count

if __name__ == "__main__":
    
    if len(sys.argv) >= 3:
        
        base = int(sys.argv[1])
        exp = int(sys.argv[2])

        power_result, multiplications_count = power(base, exp)

        print()
        print("The result is {0}".format(power_result))
        print("{0} multiplications were made.".format(multiplications_count))

    else:
        print("Missing arguments!")

