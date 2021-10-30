n = int(input())
f = [1] * 501

for i in range(2, 501):
    f[i] = f[i - 1] * i

print(len(str(f[n])) - len(str(int(str(f[n])[::-1]))))
