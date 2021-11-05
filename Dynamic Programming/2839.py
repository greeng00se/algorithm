n = int(input())
MAX = int(1e9)
sugar = [MAX] * 5001
sugar[3], sugar[5] = 1, 1

for i in range(6, 5001):
    if sugar[i - 3] != -1:
        if sugar[i] > sugar[i - 3] + 1:
            sugar[i] = sugar[i - 3] + 1
    if sugar[i - 5] != -1:
        if sugar[i] > sugar[i - 5] + 1:
            sugar[i] = sugar[i - 5] + 1

if sugar[n] == MAX:
    print(-1)
else:
    print(sugar[n])