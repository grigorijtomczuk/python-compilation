def countDuplicates(nums):
	counter = 0
	for i in nums:
		if nums.count(i) > 1:
			counter +=1
	return f"Duplicates: {counter}"	

def main():
	array = []
	arrayLength = int(input("Enter list length: "))
	for i in range(arrayLength):
		element = int(input(f"Number #{i+1}: "))
		array.append(element)
	print(array)
	print(countDuplicates(array))

if __name__ == "__main__":
	main()
