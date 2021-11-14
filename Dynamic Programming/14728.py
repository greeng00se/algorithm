n, t = map(int, input().split())

a = [0] * (t + 1)

for _ in range(n):
    k, s = map(int, input().split())
    for i in range(t, k - 1, -1):
        a[i] = max(a[i], s + a[i - k])
        
print(a[-1])