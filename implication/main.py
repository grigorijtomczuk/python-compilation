print("x y f")
for x in 0, 1:
	for y in 0, 1:
		# "x <= y" is equal to "x -> y" AND "(x and y) or not x" (check the implciation summary table)
		if x <= y:
			print(x, y, "1")
		else:
			print(x, y, "0")
