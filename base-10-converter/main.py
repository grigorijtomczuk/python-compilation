from math import log


def convertFromBase10(num, base):
	# Create conversion dictionary OR just use a string (indexed by default)
	# numToChar = {i:"0123456789ABCDEF"[i] for i in range(16)}
	numToChar = "0123456789ABCDEF"
	# Compute the power value
	power = int(log(num, base))
	# Convert number
	converted = ""
	for pow in range(power, -1, -1):
		# Floor division
		converted += numToChar[num // (base**pow)]
		# Remainder
		num %= base**pow
	# Return
	return converted


def main():
	num = int(input("Enter a decimal number to convert: "))
	base = int(input("Enter base: "))
	print(f"The converted number is {convertFromBase10(num, base)} in base {base}")


if __name__ == "__main__":
	main()
