try:
	i = int(input("Enter an integer: "))
	result = i + 5
except ValueError:  # not <int> type was entered
	print("Sometihng went wrong!")
except:  # handling any other error that may occur
	print("Something went terribly wrong!")
else:  # run if no exception was caught
	print(result)
finally:  # run anyway whether an exception was caught or not
	print("Bye!")
print("Bye once more!")  # the rest of the program goes on due to exception handling above


class SomeError(Exception):  # a custom error class
	pass


try:
	raise SomeError  # force a specified exception to occur
except SomeError:
	print("Some error occured!")
