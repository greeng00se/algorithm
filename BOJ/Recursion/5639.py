import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

data = []

def solve(n):
    if len(n) <= 1: return n
    for i in range(1, len(n)):
        if n[i] > n[0]: return solve(n[1:i]) + solve(n[i:]) + [n[0]]

    return solve(n[1:]) + [n[0]]

while True:
    try: k = int(input())
    except: break
    data.append(k)
    
data = solve(data)
for i in data: print(i)

