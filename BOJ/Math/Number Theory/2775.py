import sys

input = sys.stdin.readline 

apt = [[i for i in range(1, 16)]]
for i in range(15):
    tmp = []
    for j in range(15):
        tmp.append(sum(apt[i][:j + 1]))
    apt.append(tmp)
    
rep = int(input())
for _ in range(rep):
    k = int(input())
    n = int(input())
    print(apt[k][n - 1])