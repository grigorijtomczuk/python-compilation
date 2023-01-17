def generator(a, b):
	"""Returns a generator of [a;b] range of numbers"""
	while a <= b:
		yield a
		a += 1


g = generator(1, 3)

print(next(g))
print(next(g))
print(next(g))
print(list(g))  # prints empty list as the values of g have been all used and "erased"
