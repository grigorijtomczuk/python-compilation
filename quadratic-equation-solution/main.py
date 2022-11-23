from math import sqrt


def solveQE(a, b, c):
	D = b**2 - 4 * a * c
	if D > 0:
		x1 = (-b + sqrt(D)) / (2 * a)
		x2 = (-b - sqrt(D)) / (2 * a)
		print(f"The roots are {x1} and {x2}.")
	elif D == 0:
		x = -b / 2 * a
		print(f"The only root is {x}.")
	else:
		print("No real roots!")


def main():
	a = int(input("Enter the A value: "))
	b = int(input("Enter the B value: "))
	c = int(input("Enter the C value: "))
	solveQE(a, b, c)


if __name__ == "__main__":
	main()
