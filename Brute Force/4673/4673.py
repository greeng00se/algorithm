flag = [0] * 20002

for i in range(1, 10001):
    flag[i + sum(map(int, list(str(i))))] = 1

for i in range(1, 10000):
    if flag[i]: continue
    print(i)
