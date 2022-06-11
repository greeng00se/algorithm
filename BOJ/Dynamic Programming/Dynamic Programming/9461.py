rep = int(input())

a = [0] * 101
a[1], a[2], a[3] = 1, 1, 1
a[4], a[5] = 2, 2

for i in range(6, 101):
    a[i] = a[i - 1] + a[i - 5]

for i in range(rep):
    n = int(input())
    print(a[n])