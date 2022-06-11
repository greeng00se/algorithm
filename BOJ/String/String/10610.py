import sys

input = sys.stdin.readline

data = list(input().rstrip())
data.sort(reverse = True)
if sum(map(int, data)) % 3 != 0 or '0' not in data:
    print(-1)
else:
    print(''.join(data))
    