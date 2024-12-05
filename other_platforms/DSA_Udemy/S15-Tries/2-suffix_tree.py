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
    
    def insert_suffix_tree(self,word):
        #all suffix from word to be inserted in the Trie
        for i in range(0,len(word)):
            self.insert(word[i:])

# Simplified suffix tree
t=Trie()
t.insert_suffix_tree("hello")
print(t.search("hello"))
print(t.search("o"))
print(t.search("notthere"))