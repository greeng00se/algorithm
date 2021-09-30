n, k = map(int, input().split())

a = [0] * 100
a[0] = 1
for i in range(1, 100):
    a[i] = a[i - 1] * i
    
print(a[n] // (a[k] * a[n - k]))