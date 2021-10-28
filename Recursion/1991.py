import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

tree = {}

n = int(input())

for _ in range(n):
    a, b, c = input().rstrip().split()
    if a not in tree.keys(): tree[a] = []
    tree[a].append(b)
    tree[a].append(c)

preOrder = inOrder = postOrder = ''

def preOrderTraversal(x):
    global preOrder
    if x == '.': return
    preOrder += x    
    if tree[x][0] in tree.keys(): preOrderTraversal(tree[x][0])
    if tree[x][1] in tree.keys(): preOrderTraversal(tree[x][1])

def inOrderTraversal(x):
    global inOrder
    if x == '.': return
    if tree[x][0] in tree.keys(): inOrderTraversal(tree[x][0])
    inOrder += x    
    if tree[x][1] in tree.keys(): inOrderTraversal(tree[x][1])
        
def postOrderTraversal(x):
    global postOrder
    if x == '.': return
    if tree[x][0] in tree.keys(): postOrderTraversal(tree[x][0])
    if tree[x][1] in tree.keys(): postOrderTraversal(tree[x][1])
    postOrder += x    
    
    
preOrderTraversal('A')
inOrderTraversal('A')
postOrderTraversal('A')
    
print(preOrder)
print(inOrder)
print(postOrder)
    
    