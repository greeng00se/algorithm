n = int(input())

data = []
alpha = {}
alphaValue = [0] * 26
result = 0

def getIndex(s):
    return ord(s) - ord('A')

for _ in range(n):
    strings = input()
    data.append(strings)
    v = 1
    for s in strings[::-1]:
        if not s in alpha.keys():
            alpha[s] = 0
        alpha[s] += v
        v *= 10
        
alpha = sorted(alpha.items(), key = lambda x : x[1], reverse = True)
v = 9
for s in alpha:
    alphaValue[getIndex(s[0])] = v
    v -= 1
    
for i in range(n):
    v = 1
    for s in data[i][::-1]:
        result += alphaValue[getIndex(s)] * v
        v *= 10
        
print(result)