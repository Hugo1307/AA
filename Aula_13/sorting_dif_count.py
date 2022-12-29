def main():

    lines = []

    with open("aleatorios000020000.txt", "r") as f:
        lines = f.readlines()  

    lines.sort()

    count = 0
    last_line = None
    for line in lines:
        if last_line and last_line != line:
            count += 1
        last_line = line 
    
    print(count)

if __name__ == "__main__":
    main()
