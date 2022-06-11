import sys

input = sys.stdin.readline

def solve(crain, box):
    if max(crain) < max(box):
        return -1

    result = 0

    while box:
        for c in crane:
            for b in box:
                if c >= b:
                    box.remove(b)
                    break
            
        result += 1
    
    return result

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crane.sort(reverse = True)
box.sort(reverse = True)

print(solve(crane, box))