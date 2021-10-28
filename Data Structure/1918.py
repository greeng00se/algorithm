import sys

input = sys.stdin.readline

data = list(input())
result = ''
s = []
for c in data:
    if c.isalpha(): result += c; continue
    if c == '(': s.append(c)
    if c in ')':
        while s and s[-1] not in '(':
            result += s.pop()
        if s and s[-1] in '(': s.pop()
    if c in '*/':
        while s and s[-1] in '*/': 
            result += s.pop()
        s.append(c)
    if c in '+-':
        while s and s[-1] not in '(':
            result += s.pop()
        s.append(c)
        
while s:
    if s[-1] in '()': s.pop(); continue
    result += s.pop()
print(result)

# 1. Operand -> output
# 2. ( -> stack
# 3. ) -> stack.pop() until ( and remove (
# 4. op -> stack.pop() until lower priority than op, (, stack.empty() and then push op
# 5. Pop all the elements in the stack when input ends.
# 6. Priority : (, ) > *, / > +, -
    