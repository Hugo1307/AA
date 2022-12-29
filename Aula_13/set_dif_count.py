import cProfile

def main():

    lines = []

    with open("aleatorios000020000.txt", "r") as f:
        lines = f.readlines()  

    my_set = set(lines)
    print(len(my_set))

if __name__ == "__main__":
    cProfile.run("main()")