import sys

input = sys.stdin.readline

h, w = map(int, input().split())
data = list(map(int, input().split()))

left, right = [0] * w, [0] * w
result = 0

for i in range(w):
    left[i] = max(max(left), data[i])
    right[w - i - 1] = max(max(right), data[w - i - 1])
    
for i in range(w):
    result += max(0, min(left[i], right[i]) - data[i])
    
print(result)