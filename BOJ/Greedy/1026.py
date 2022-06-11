import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse = True)

result = 0

for pair in zip(a, b):
    result += (lambda x, y: x * y)(pair[0], pair[1])
    
print(result)