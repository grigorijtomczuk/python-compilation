from math import fmod

print(10 // 3)  # 3
print(10 % 3)  # 1

# Python: intDiv = math.floor(n / base)
# C, Java, ...: intDiv = int(n / base)
print((-10) // 3)  # -4

# Python: mod = n - math.floor(n / base) * base
# C, Java, ...: mod = n - int(n / base) * base -> Python's math.fmod() method
print((-10) % 3, fmod(-10, 3))  # 2 -1.0

print(10 // (-3))  # -4
print(10 % (-3), fmod(10, -3))  # -2 1.0
