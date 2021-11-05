import sys

input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    call = int(input())
    if call != 0:
        stack.append(call)
    if stack and call == 0:
        stack.pop()
        
print(sum(stack))