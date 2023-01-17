def decorator(func):

	def wrapper():
		print("Before main func")
		func()
		print("After main func")
		return

	return wrapper


@decorator  # talk = decorator(talk)
def talk():
	print("Hello!")


talk()
