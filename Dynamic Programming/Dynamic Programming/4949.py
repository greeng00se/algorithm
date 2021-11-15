import sys

input = sys.stdin.readline

while True:
    strings = list(input().rstrip())
    if len(strings) == 1 and strings[0] == '.':
        break
    stack = []
    flag = 1
    for i in strings:
        if i in '([':
            stack.append(i)
        if i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = 0
                break
        if i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = 0
                break
                
    if flag and not stack:
        print('yes')
    else:
        print('no')