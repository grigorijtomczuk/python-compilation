generator = (x * x for x in range(1, 4))
for i in generator:
	print(i)
for i in generator:  # won't execute 2nd time as the values of generator are not stored in memory
	print(i)
