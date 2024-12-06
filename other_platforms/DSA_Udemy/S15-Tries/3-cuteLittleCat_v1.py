# We want to know if a word from words in present in document
# Idea1: create a suffix tree from 0..len(document) and search the words in the suffix tree (but using startsWith)
# O(D^2): create trie
# O(WN): search

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
    
    def startsWith(self,word):
        node=self.root
        for c in word:
            if c not in node.children:
                return False
            node=node.children[c]
        return True

    def insert_suffix_tree(self,word):
        for i in range(0,len(word)):
            self.insert(word[i:])

# Using suffix tree
document="little cute cat loves to code in c++, java & python"
words=["cute cat", "ttle", "cutest", "cat", "quick", "big"] #T,T,F,T,F,F

t=Trie()
t.insert_suffix_tree(document)
for w in words:
    print(t.startsWith(w))