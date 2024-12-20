import random 
import string
class Codec:

    def __init__(self):
        self.hm={}
        self.hm_r={}

    def encode(self, longUrl: str) -> str:
        if longUrl in self.hm:
            return self.hm[longUrl]
        
        chars=string.ascii_letters+string.digits
        seq=''.join(random.choices(chars,k=5))
  
        self.hm_r[seq]=longUrl
        self.hm[longUrl]=seq

        return seq        

    def decode(self, shortUrl: str) -> str:
        return self.hm_r[shortUrl]
        

codec = Codec()
print(codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl")))