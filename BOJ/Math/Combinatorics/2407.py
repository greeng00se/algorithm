n, m = map(int, input().split())

f = [1] * 101
for i in range(2, 101): 
    f[i] = f[i - 1] * i

nPr = f[n] // f[n - m]
print(nPr // f[m])