from datetime import datetime
from os import path


def printFile(file: str) -> None:
	with open(file, "r") as f:
		count = 0
		for line in f:
			count += 1
			print(f"Line #{count}: \"{line.strip()}\"\n")
		f.close()


def getFilename(file: str) -> str:
	return path.basename(file)


def getDateTime():
	now = datetime.now()
	return now.strftime("%Y/%m/%d %H:%M:%S")


def duplicateFile(file1: str, file2: str) -> None:
	with open(file1, "r") as f1:
		with open(file2, "w") as f2:
			f2.write(f"[DUPLICATED {getFilename(f1.name)} {getDateTime()}]\n{f1.read()}")
			print(f"Your file has been successfully duplicated to {getFilename(f2.name)}!")
			f2.close()
		f1.close()


def main():
	printFile("./text.txt")
	input("Press enter to duplicate the file... ")
	duplicateFile("./text.txt", "./text1.txt")


if __name__ == "__main__":
	main()
