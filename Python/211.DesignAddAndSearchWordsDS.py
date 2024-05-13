class TrieNode:
    def __init__(self):
        self.children={}
        self.EOW=False #end of word

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        node=self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node=node.children[char]
        node.EOW = True        

    def search(self, word: str) -> bool:
        def search_int(subword:str,node=self.root) -> bool:
            if len(subword)==0:
                return node.EOW
            ch=subword[0]
            if ch=='.':
                ans=False
                for child in node.children:
                    ans=ans or search_int(subword[1:],node.children[child])
                return ans
            elif ch not in node.children: return False
            return search_int(subword[1:],node.children[ch])
        return search_int(word)


wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad")) # False
print(wordDictionary.search("bad")) # True
print(wordDictionary.search(".ad")) # True
print(wordDictionary.search("b..")) # True
print(wordDictionary.search("d.p")) # False