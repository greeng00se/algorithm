import sys
from collections import deque

input = sys.stdin.readline

rep = int(input())

def AC(f, s):
    r = 0
    for op in f:
        if op == 'R':
            r = r ^ 1
        if op == 'D':
            if s and not r: s.popleft()
            elif s and r: s.pop()
            else: 
                print('error')
                return
            
    if r: s.reverse()
    print('['+','.join(s)+']')
    
for _ in range(rep):
    f = map(str, input().rstrip())
    n = int(input())
    s = list(input().rstrip().lstrip('[').rstrip(']').split(','))
    q = deque(s)
    if q[0] == '':
        q.popleft()
    AC(f, q)
    

                
    