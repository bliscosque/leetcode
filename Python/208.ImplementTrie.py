from string import ascii_letters

class TrieNode:
    def __init__(self):
        self.is_word=False
        self.s = {c:None for c in ascii_letters}

class Trie:
    def __init__(self):
        self.tn = TrieNode()

    def insert(self, word: str) -> None:
        def ins_int(tn,i=0):
            if tn is None:
                tn=TrieNode()
            if i==len(word):
                tn.is_word=True
            else:
                tn.s[word[i]]=ins_int(tn.s[word[i]],i+1)
            return tn        
        ins_int(self.tn,0)

    def search(self, word: str) -> bool:
        def search_int(tn,i=0):
            if tn is None: return False
            if i==len(word):
                if tn.is_word:
                    return True
                else:
                    return False
            return search_int(tn.s[word[i]],i+1)
        return search_int(self.tn,0)

    def startsWith(self, prefix: str) -> bool:
        def search_int(tn,i=0):
            if tn is None: return False
            if i==len(prefix):
                return True
            return search_int(tn.s[prefix[i]],i+1)
        return search_int(self.tn,0)


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
obj.insert("app")
print(obj.search("app"))