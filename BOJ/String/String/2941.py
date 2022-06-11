import sys

input = sys.stdin.readline

string = list(input().rstrip())
i, length = 0, len(string)
result = 0

while i < length:
    if i <= length - 2 and string[i] + string[i + 1] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
        i += 2
    elif i <= length - 3 and string[i] + string[i + 1] + string[i + 2] == 'dz=':
        i += 3
    else:
        i += 1
    result += 1

print(result)