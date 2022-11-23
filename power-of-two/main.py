# Creates an exponent table for number 2
print(f"Exponent{' ' * 2}Number")
for pow in range(17):
	print(f"{pow}{' ' * (10 - len(str(pow)))}{2**pow}")
