import sys

input = sys.stdin.readline

rep = int(input())
data = ['9999999999999999999'] * 101

data[2] = '1'
data[3] = '7'
data[4] = '4'
data[5] = '2'
data[6] = '6'
data[7] = '8'
sv = ['99999999', '99999999', '1', '7', '4', '2', '0', '8']

for i in range(8, 101):
    for j in range(2, 8):
        data[i] = str(min(int(data[i]), int(data[i - j] + sv[j])))
        
def makehigh(n):
    result = ''
    if n % 2 != 0:
        n -= 3
        result += '7'
        
    if n == 0: return result
    result += '1' * (n // 2)
    return result
    
def makelow(n):
    return data[n]
    
def match(n):
    l = makelow(n)
    h = makehigh(n)
    
    return l, h

for i in range(rep):
    n = int(input())
    l, h = match(n)
    print(l, h)