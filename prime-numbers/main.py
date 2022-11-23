# Computes and prints a list of prime numbers
list = []
for num in range(2, 101):
	prime = True
	for divisor in range(2, int(num**0.5) + 1):
		if (num % divisor) == 0:
			prime = False
			break
	if prime:
		list.append(num)

print(list)
