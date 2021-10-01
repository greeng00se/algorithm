import sys

input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))
result = int(1e9)

check, end = 0, 0

for start in range(n):
    while check < s and end < n:
        check += data[end]
        end += 1
    if check >= s:
        result = min(result, end - start)
    check -= data[start]
    
if result == int(1e9):
    print(0)
else:
    print(result)