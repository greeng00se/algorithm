import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    data = list(map(int, input().split()))

    if n == 1:
        print('A')
        return
    if n == 2:
        if data[0] == data[1]: print(data[0])
        else: print('A')
        return
    
    flag = 1
    a = 0
    x = data[1] - data[0]
    y = data[2] - data[1]
    if x: a = y // x
    b = data[1] - a * data[0]
    for i in range(1, n):
        if data[i] != data[i - 1] * a + b:
            flag = 0
            break
    
    if flag: print(data[-1] * a + b)
    else: print('B')
        
solve()