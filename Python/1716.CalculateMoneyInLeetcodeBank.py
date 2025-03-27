class Solution:
    def totalMoney(self, n: int) -> int:
        v_last_week=1
        last_v=1
        ans=0
        for i in range(n):
            if i>0 and i%7==0:
                last_v=v_last_week+1
                v_last_week+=1
            ans+=last_v
            #print(last_v)
            last_v+=1
        return ans

s=Solution()
#print(s.totalMoney(4)) #10
#print(s.totalMoney(10)) #37
print(s.totalMoney(20)) #96