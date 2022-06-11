import sys

input = sys.stdin.readline

n = int(input())
data = sorted(list(map(int, input().split())))
result = 0

for i in range(n):
    l, r = 0, n - 1
    while l < r:
        s = data[l] + data[r]
        if s == data[i]:
            if l == i: l += 1
            elif r == i: r -= 1
            else:
                result += 1
                break
        elif s > data[i]:
            r -= 1
        else:
            l += 1

print(result)
