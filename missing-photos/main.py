import os
from glob import glob


def alphaSlice(fileName: str) -> str:
	"""Get file's alphabetic part."""
	alpha = ""
	for char in fileName:
		if char == ".":
			break
		if not char.isdigit():
			alpha += char
	return alpha


def numSlice(fileName: str) -> int:
	"""Get file's numeric part."""
	num = ""
	for char in fileName:
		if char.isdigit():
			num += char
	return int(num)


def extSlice(fileName: str) -> str:
	"""Get file's extension (e.g. ".txt", ".jpg")."""
	return os.path.splitext(fileName)[1]


def main():
	DIRECTORY = os.path.dirname(__file__)
	PATTERN = "./DSCF*.JPG"  # Use regular expression

	fileNameList = [os.path.basename(f) for f in glob(PATTERN, root_dir=DIRECTORY)]
	missedFileList = []

	for i in range(len(fileNameList) - 1):
		x = 1
		while numSlice(fileNameList[i]) + x != numSlice(fileNameList[i + 1]):
			missedFileName = alphaSlice(fileNameList[i]) + str(numSlice(fileNameList[i]) + x) + extSlice(fileNameList[i])
			missedFileList.append(missedFileName)
			x += 1

	print(f"Missing photos found: {len(missedFileList)}")
	print(*missedFileList, sep=", ")


if __name__ == "__main__":
	main()
