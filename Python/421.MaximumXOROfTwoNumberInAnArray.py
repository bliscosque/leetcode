from typing import List
class TrieNode:
    def __init__(self):
        self.children={}
        self.num=0

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,num):
        nbin=format(num&0xFFFFFFFF, '032b')
        node=self.root
        for d in nbin:
            if d not in node.children:
                node.children[d]=TrieNode()
            node=node.children[d]
        node.num=num

    def search_max_xor(self,num):
        nbin=format(num&0xFFFFFFFF, '032b')
        node=self.root
        for d in nbin:
            oposite='1' if d=='0' else '0'
            if oposite in node.children:
                node=node.children[oposite]
            elif d in node.children:
                node=node.children[d]
            else: 
                return 0
        #print(num, node.num)
        return node.num


    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        t=Trie()
        for n in nums:
            t.insert(n)
        max_xor=0
        for n in nums:
            max_xor=max(max_xor,n^t.search_max_xor(n))
        return max_xor

s=Solution()
print(s.findMaximumXOR([3,10,5,25,2,8])) #28 (5 XOR 25)
print(s.findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70])) # 127
print(s.findMaximumXOR([1])) #0