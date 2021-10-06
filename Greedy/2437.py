n = int(input())
a = list(map(int, input().split()))
a.sort()
t = 1
for c in a:
    if t < c:
        break
    t += c
    
print(t)