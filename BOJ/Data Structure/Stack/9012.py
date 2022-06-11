import sys

input = sys.stdin.readline

rep = int(input())

for _ in range(rep):
    strings = list(input().rstrip())
    stack = []
    flag = 1
    for letter in strings:
        if letter == '(':
            stack.append(letter)
        if letter == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = 0
                
    if flag and not stack:
        print('YES')
    else:
        print('NO')