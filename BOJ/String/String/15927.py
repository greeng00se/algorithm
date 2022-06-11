import sys

input = sys.stdin.readline

n = input().rstrip()
nr = n[::-1]
result = -1

if n == nr:
    for i in range(1, len(n)):
        if n[0] == n[i]: 
            continue
        else:
            result = len(n) - 1
            break
else:
    result = len(n)

print(result)
