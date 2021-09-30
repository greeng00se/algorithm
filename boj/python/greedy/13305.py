n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0
r = a[0]
minValue = b[0]
for i in range(1, len(a)):
    if minValue > b[i]:
        result += r * minValue
        minValue = b[i]
        r = 0
    r += a[i]

if r:
    result += r * minValue
    
print(result)