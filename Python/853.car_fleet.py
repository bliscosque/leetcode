from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ltup=list(zip(position,speed))
        ltup.sort()
        ans=0
        i=len(ltup)-1
        while i>=0:
            #print(i)
            ans+=1
            p=ltup[i][0]
            s=ltup[i][1]
            time=(target-p)/s
            n_i=i-1

            # while before vehicules arrive in less time, they form a fleet with prev one
            while n_i>=0:
                p_n=ltup[n_i][0]
                s_n=ltup[n_i][1]
                time_n=(target-p_n)/s_n
                #print(time, n_i,time_n)
                if time_n<=time:
                    #print("ck")
                    i-=1
                    n_i-=1
                else:
                    break
            
            i-=1
            
        return ans

s=Solution()
print(s.carFleet(12,[10,8,0,5,3], [2,4,1,1,3]))
print(s.carFleet(10,[3], [3]))
print(s.carFleet(100,[0,2,4], [4,2,1]))