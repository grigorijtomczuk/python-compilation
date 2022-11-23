# Computes and prints the byte representation of num (given in bits)

num = 160 * 160 * 8

print(f"Bits: {num}")
print(f"Bytes: {num / 8} OR {num / 2**3}")
print(f"KBytes: {(num / 8) / 1024} OR {num / 2**13}")
print(f"Mbytes: {((num / 8) / 1024) / 1024} OR {num / 2**23}")
print(f"GBytes: {(((num / 8) / 1024) / 1024) / 1024} OR {num / 2**33}")
