def main():

	lines = []

	with open("aleatorios000020000.txt", "r") as f:
		lines = f.readlines()  

	bitmap = [0] * len(lines)

	for lineIdx in range(0, lines):
		bitmap[lineIdx] = 1


if __name__ == "__main__":
	main()
