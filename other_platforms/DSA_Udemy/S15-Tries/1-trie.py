class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word):
        node=self.root
        for c in word:
            if c not in node.children:
                node.children[c]=TrieNode()
            node=node.children[c]
        node.is_end=True

    def search(self,word):
        node=self.root
        for c in word:
            if c not in node.children:
                return False
            node=node.children[c]
        return node.is_end

t=Trie()
t.insert("Try1")
t.insert("new")
print(t.search("Tr"))
print(t.search("Try1"))
print(t.search("Try12"))
