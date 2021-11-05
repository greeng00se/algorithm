import sys

input = sys.stdin.readline

rep = int(input())
stack = []
for _ in range(rep):
    op = list(input().split())
    
    if op[0] == 'push':
        stack.append(int(op[1]))
    if op[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    if op[0] == 'size':
        print(len(stack))
    if op[0] == 'empty':
        print(0 if stack else 1)
    if op[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
        