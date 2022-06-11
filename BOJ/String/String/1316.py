import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
result = 0

for _ in range(n):
    d = defaultdict(int)
    string = input()
    isGroupWord = 1
    flag = string[0]
    d[flag] += 1
    
    for i in range(1, len(string)):
        if flag != string[i] and d[string[i]]:
            isGroupWord = 0
            break
        flag = string[i]
        d[flag] += 1
        
    if isGroupWord: result += 1
        
print(result)

            