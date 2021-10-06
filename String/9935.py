import sys

input = sys.stdin.readline
s = list(input().rstrip())
b = list(input().rstrip())

def check():
    for i in range(len(b)):
        if b[-(i + 1)] != q[-(i + 1)]:
            return False
    return True

q = []
for i in s:
    q.append(i)
    if len(q) < len(b):
        continue
    if check():
        for i in range(len(b)):
            q.pop()
            
if q: print(''.join(q))
else: print('FRULA')