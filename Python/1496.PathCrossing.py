class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pntlist=set()
        pnt=(0,0)
        pntlist.add(pnt)
        for mv in path:
            #print(mv,pnt,pntlist)
            if mv=='N': x,y=(0,1)
            elif mv=='S': x,y=(0,-1)
            elif mv=='E': x,y=(1,0)
            else: x,y=(-1,0)
            pnt=(pnt[0]+x,pnt[1]+y)
            if pnt in pntlist: return True
            pntlist.add(pnt)
        return False

s=Solution()
print(s.isPathCrossing("NES")) #False
print(s.isPathCrossing("NESWW")) #True