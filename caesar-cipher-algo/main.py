def encrypt(message: str, key: int = 3) -> str:
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	result = ""
	for char in message.upper():
		if char == " ":
			result += " "
		else:
			position = (alphabet.find(char) + key) % len(alphabet)
			result += alphabet[position]
	return result

print(encrypt("Caesar Cipher Demo"))
