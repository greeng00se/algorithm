import re
for i in range(int(input())):print('YES'if re.fullmatch('(100+1+|01)+',input())else'NO')