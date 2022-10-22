from math import log

def convertFromBase10(num, base):
	numToChar = "0123456789ABCDEF"
	power = int(log(num, base))
	converted = ""
	for pow in range(power, -1, -1):
		converted += numToChar[num // (base**pow)]
		num %= base**pow
	return converted

num = int(input("Enter a number: "))
base = int(input("Enter a base to convert to: "))
print(convertFromBase10(num, base))
