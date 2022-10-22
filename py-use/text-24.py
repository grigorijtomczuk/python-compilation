with open("24.txt") as f:
    p = f.readline()
    max_len = 0
    cur_len = 0
    for i in range(len(p) - 1):
        if p[i] == "X" and p[i + 1] == "Z" and p[i + 2] == "Z" and p[i + 3] == "Y":
            if max_len < cur_len:
                max_len = cur_len
            cur_len = 3
        else:
            cur_len += 1
    if max_len < cur_len:
        max_len = cur_len
    print(max_len)
