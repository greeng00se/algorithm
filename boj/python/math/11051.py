n, k = map(int, input().split())

a = [0] * 1001
a[0] = 1
for i in range(1, 1001):
    a[i] = a[i - 1] * i
    
print(a[n] // (a[k] * a[n - k]) % 10007)