def getSum(numBin):
	sum = 0
	for i in range(len(numBin)):
		sum += int(numBin[i])
	return sum

for n in range(100):
	nBin = str(bin(n))[2:]
	sum = getSum(nBin)
	nBin += str(sum % 2)
	sum = getSum(nBin)
	nBin += str(sum % 2)
	conv = int(nBin, 2)
	if conv > 123:
		print(conv)
		break
