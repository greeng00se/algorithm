n = int(input())
a = list(map(int, input().split()))

r = [0] * (n + 1)
for i in range(1, n + 1):
    s = 0
    for j in range(1, i):
        if a[i - 1] > a[j - 1] and r[j] > r[s]:
            s = j
            
    r[i] = r[s] + 1
    
print(max(r))
        