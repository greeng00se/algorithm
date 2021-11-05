import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
stack = []
answer = []
seq = [int(input()) for _ in range(n)]
now = 0
for i in range(1, n + 1):
    stack.append(i)
    answer.append('+')
    while stack and now < n and stack[-1] == seq[now]:
        now += 1
        answer.append('-')
        stack.pop()

count = Counter(answer)
if count['+'] == count['-']:
    for i in answer: print(i)
else:
    print('NO')
    
    