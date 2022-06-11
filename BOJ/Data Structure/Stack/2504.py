import sys

input = sys.stdin.readline

data = list(input().rstrip())
answer = 0         
d = {'(': 2, ')': 2, '[': 3, ']': 3}
def solve(strings):
    result = 0
    coiff = 1
    stack = []
    
    for i in range(len(strings)):
        letter = strings[i]
        if letter in '[(':
            stack.append(letter)
            coiff *= d[letter]
            continue
        
        if stack and letter == ']' and stack[-1] == '[':
            if strings[i - 1] == '[': result += coiff
        elif stack and letter == ')' and stack[-1] == '(':
            if strings[i - 1] == '(': result += coiff
        else: return -1
        stack.pop()
        coiff //= d[letter]
    if stack: return -1
    return result

answer = solve(data)
print(answer if answer != -1 else 0)
            
        
