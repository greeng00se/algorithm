from bisect import bisect_left, bisect_right
n, m = map(int, input().split())

h1, h2 = [], []

for i in range(n // 2):
    h1.append(int(input()))
    h2.append(int(input()))
    
h1.sort(), h2.sort()

result = []

for i in range(m):
    a = bisect_left(h1, i + 1)
    b = bisect_right(h2, m - i - 1)
    result.append(n - a - b)
    
result.sort()
print(min(result), bisect_right(result, min(result)) - bisect_left(result, min(result)))
    
