import sys

multiplications_counter = 0

def power(a,b):

    global multiplications_counter

    if b == 1:
        return a

    if b % 2 == 0:
        multiplications_counter += 1
        return power(a, b/2) * power(a, b/2)
    else:
        multiplications_counter += 1
        return power(a, b//2) * power(a, (b//2)+1)

def main():

    if len(sys.argv) >= 3:

        base = int(sys.argv[1])
        exp = int(sys.argv[2])

        result = power(base, exp)

        print()
        print("The result is {0}".format(result))
        print("{0} multiplications were made".format(multiplications_counter))

    else:
        print("Missing Arguments")
        

if __name__ == "__main__":
    main()