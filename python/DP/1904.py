N = int(input())
a = [0] * 1000001
a[1] = 1
a[2] = 2
for i in range(3, N + 1):
    a[i] = (a[i - 1] + a[i - 2]) % 15746
print(a[N])