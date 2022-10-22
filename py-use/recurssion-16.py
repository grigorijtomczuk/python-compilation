def function(n):
	if n == 1:
		return 1
	if n == 2:
		return 2
	if n > 2:
		return function(n-1) - function(n-2) + 2 * n

print(function(6))