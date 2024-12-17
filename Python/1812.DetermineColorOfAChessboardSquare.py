class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        p1,p2=ord(coordinates[0])-ord('a'),int(coordinates[1])
        if p1%2==1:
            return p2%2!=0
        return p2%2==0


s=Solution()
print(s.squareIsWhite("a1")) #False (black)
print(s.squareIsWhite("h3")) #True (white)
print(s.squareIsWhite("c7")) #False (Black)