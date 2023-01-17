def count():

	def increment_counter():
		nonlocal count
		count += 1
		return count

	count = 0
	return increment_counter


increment_counter = count()

print(increment_counter())
print(increment_counter())
print(increment_counter())
