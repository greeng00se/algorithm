import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
pos = [0] * (n + 1)
for i in range(n):
    pos[inorder[i]] = i
    
def preorder(in_l, in_r, post_l, post_r):
    if in_l > in_r or post_l > post_r:
        return
    
    parents = postorder[post_r]
    print(parents, end = ' ')
    
    l = pos[parents] - in_l
    r = in_r - pos[parents]
    
    preorder(in_l, in_l + l - 1, post_l, post_l + l - 1)
    preorder(in_r - r + 1, in_r, post_r - r, post_r - 1)
    
preorder(0, n - 1, 0, n - 1)
print()