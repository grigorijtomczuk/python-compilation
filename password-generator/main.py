from datetime import datetime
from random import randint


def generatePassword(passwordLength: int) -> str:
	charSet = "0123456789abcdefABCDEF!@#$%^&*_"
	# charToNum = {i: charSet[i] for i in range(len(charSet))}
	password = ""
	for i in range(passwordLength):
		password += charSet[randint(0, len(charSet) - 1)]
	return password


def getDateTime() -> str:
	now = datetime.now()
	return now.strftime("%Y/%m/%d %H:%M:%S")


def saveToFile(item: str, file: str) -> None:
	with open(file, "a") as f:
		f.write(f"{item} [{getDateTime()}]\n")
		f.close()
	print("Your password has been successfully saved!")


def main():
	passwordLength = int(input("Password length: "))
	password = generatePassword(passwordLength)
	saveToFile(password, "./password.txt")


if __name__ == "__main__":
	main()
