import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
q = list(map(int, input().split()))

def countByRange(num):
    return bisect_right(cards, num) - bisect_left(cards, num)

for number in q:
    if countByRange(number): print(1, end = ' ')
    else: print(0, end = ' ')
print()