import sys

input = sys.stdin.readline

rep = int(input())

for _ in range(rep):
    h, w, n = map(int, input().split())
    floor = n % h
    room = n // h + 1
    if floor == 0: 
        floor = h
        room -= 1
    
    print(floor, room if room >= 10 else '0' + str(room) , sep = '')