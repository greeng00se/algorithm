import sys

input = sys.stdin.readline

class Node(object):
    def __init__(self, key):
        self.key = key
        self.children = {}
        
class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, strings):
        current_node = self.head

        for string in strings:
            if string not in current_node.children:
                current_node.children[string] = Node(string)
            current_node = current_node.children[string]

    def search(self):
        current_node = self.head
        strings = sorted(current_node.children.items())
        for string in strings:
            self.dfs(current_node.children[string[0]], 0)
            
    def dfs(self, node, depth):
        current_node = node
        print('--' * depth, current_node.key, sep = '')
        strings = sorted(current_node.children.items())
        for string in strings:
            nxt = current_node.children[string[0]]
            self.dfs(nxt, depth + 1)
        
rep = int(input())
trie = Trie()
for _ in range(rep):
    strings = input().split()
    trie.insert(strings[1:])
trie.search()
    

    