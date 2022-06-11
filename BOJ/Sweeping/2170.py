import sys

input = sys.stdin.readline

n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort()
result = 0
ls, le = lines[0][0], lines[0][1]

for i in range(1, n):
    s, e = lines[i]
    if s <= le: 
        le = max(e, le)
    else:
        result += le - ls
        ls, le = s, e

result += le - ls
        
print(result)
