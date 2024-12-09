# We want to know if a word from words in present in document
# Idea: Insert all words in the Trie
# For substrings [0..n :] of document, search it in Trie
# Keep a Hashmap with words and if they're present

class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False
    
class Trie:
    def __init__(self, hm):
        self.root=TrieNode()
        self.hm=hm

    def insert(self,word):
        node=self.root
        for c in word:
            if c not in node.children:
                node.children[c]=TrieNode()
            node=node.children[c]
        node.is_end=True

    def search(self,word):
        node=self.root
        pword=""
        for c in word:
            pword+=c
            if c not in node.children:
                return
            node=node.children[c]
            if node.is_end:
                self.hm[pword]=True

    
document="little cute cat loves to code in c++, java & python"
words=["cute cat", "ttle", "cutest", "cat", "quick", "big"] #T,T,F,T,F,F


hm={w:False for w in words}
t=Trie(hm)
for w in words:
    t.insert(w)
for i in range(0,len(document)):
    t.search(document[i:])
for w in words:
    print(hm[w])