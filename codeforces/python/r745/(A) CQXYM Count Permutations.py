import sys
 
input = sys.stdin.readline
 
rep = int(input())
a = [0] * 200002
a[1] = 1
a[2] = 1
for i in range(3, 200002):
    a[i] = (a[i - 1] * i) % 1000000007
    
for i in range(rep):
    n = int(input())
    print(a[n * 2])
