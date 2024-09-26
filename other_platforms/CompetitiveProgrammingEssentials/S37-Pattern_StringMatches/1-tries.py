class TrieNode:
    def __init__(self) -> None:
        self.children={}
        self.is_end=False

class Trie:
    def __init__(self) -> None:
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
    
    def starts_with(self,prefix):
        node=self.root
        for c in prefix:
            if c not in node.children:
                return False
            node=node.children[c]
        return True
    