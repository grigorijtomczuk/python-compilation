def create_generator():
	my_range = range(1, 4)
	for n in my_range:
		yield n


g = create_generator()
print(g)  # a generator object!
for i in g:
	print(i)

print(list(g))  # prints empty list (generator exhausted)
