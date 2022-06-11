import sys

input = sys.stdin.readline

n, h = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(n)]

MAX_HP = int(1e12) * 123456

l, r = 1, MAX_HP
result = MAX_HP

while l <= r:
    mid = (l + r) // 2
    at = h
    hp = mid

    for room in rooms:
        rt, attack, health = room
        if rt == 1:
            hp -= (health // at) * attack if health % at else (health // at - 1) * attack
        else:
            at += attack
            hp = min(mid, hp + health)
        
        if hp <= 0:
            break
    
    if hp <= 0:
        l = mid + 1
    else:
        result = min(result, mid)
        r = mid - 1

print(result)

