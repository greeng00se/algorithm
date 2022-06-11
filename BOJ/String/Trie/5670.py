import sys

input = sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        
class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def search(self, string):
        current_node = self.head
        result = 0
        
        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
                if len(current_node.children) > 1 or current_node.data:
                    result += 1
        return result
    
while True:
    trie = Trie()
    strings = []
    result = 0.0
    
    try: n = int(input())
    except: break
        
    for _ in range(n):
        w = input().rstrip()
        trie.insert(w)
        strings.append(w)
        
    for w in strings:
        result += trie.search(w)
        
    print('%.2f' %(result / n))