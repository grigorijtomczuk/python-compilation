for i in range(2000000, 3000001):
    sqrti = i**0.5 
    k = 0
    for j in range(1, round(sqrti)):
        if i % j == 0:
            if (abs(i / j) - j) <= 115:
                k += 1
    if k > 2: print(i)
    k = 0
