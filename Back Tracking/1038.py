import sys

input = sys.stdin.readline

n = int(input())
data = []

def solve(now, length):
    if 1 <= length:
        data.append(int(now))
    
    for i in range(10):
        if now == '' or int(now[-1]) > i:
            nxt = now + str(i)
            solve(nxt, length + 1)
        
solve('', 0)
data.sort()
if n >= len(data): print(-1)
else: print(data[n])