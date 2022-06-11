n = int(input())

a = [[0] * 10 for i in range(101)]
a[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(2, n + 1):
    for j in range(10):
        if j != 9:
            a[i][j + 1] += a[i - 1][j]
        if j != 0:
            a[i][j - 1] += a[i - 1][j]
print(sum(a[n]) % 1000000000)