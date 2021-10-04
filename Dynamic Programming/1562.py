n = int(input())

a = [[[0] * 1024 for _ in range(10)] for _ in range(101)]

for i in range(1, 10):
    a[1][i][1 << i] = 1

for i in range(2, n + 1):
    for j in range(10):
        for k in range(1024):
            if a[i - 1][j][k] == 0:
                continue
            if j != 9:
                if k & (1 << (j + 1)):
                    a[i][j + 1][k] += a[i - 1][j][k]
                else:
                    a[i][j + 1][k + (1 << (j + 1))] += a[i - 1][j][k]
            if j != 0:
                if k & (1 << (j - 1)):
                    a[i][j - 1][k] += a[i - 1][j][k]
                else:
                    a[i][j - 1][k + (1 << (j - 1))] += a[i - 1][j][k]

result = 0
for i in range(10):
    result += a[n][i][1023]

print(result % 1000000000)
