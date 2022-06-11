n = int(input())

result = 0
for i in range(0, 1000001):
    if i >= n: break
    if n == i + sum(list(map(int, list(str(i))))):
        result = i
        break
        
print(result)