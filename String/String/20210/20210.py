import sys
import re
from functools import cmp_to_key

input = sys.stdin.readline

n = int(input())
data = [re.findall('\d+|[a-zA-Z]', input().rstrip()) for _ in range(n)]
alpha = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'

def cmp(a, b):
    for i in range(min(len(a), len(b))):
        if a[i].isalpha() and b[i].isalpha():
            diff = alpha.index(a[i]) - alpha.index(b[i])
            if diff != 0: 
                return diff
        elif a[i].isdigit() and b[i].isalpha():
            return -1
        elif a[i].isalpha() and b[i].isdigit():
            return 1
        else:
            x = int(a[i])
            y = int(b[i])
            if x == y: 
                if len(a[i]) == len(b[i]):
                    continue
                return len(a[i]) - len(b[i])
            return x - y
    return len(a) - len(b)

data.sort(key=cmp_to_key(cmp))

for result in data:
    print(''.join(result))