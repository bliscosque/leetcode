# starting from a node, we need to create a cycle passing by all other nodes and returning to the original node, minimizing the cost.

def tsp(dist):
    n=len(dist)
    dp={}
    def tsp_int(setOfCities, city):
        if (setOfCities,city) in dp:
            return dp[(setOfCities,city)]
        if setOfCities == (1<<n)-1: #all cities are visited
            return dist[city][0] #return the "comming back" cost
        
        ans=float('inf')
        for choice in range(n):
            if (setOfCities & (1<<choice))==0: # choice is not visited
                subProb=dist[city][choice]+tsp_int(setOfCities|(1<<choice), choice)
                ans=min(ans,subProb)
        dp[(setOfCities,city)]=ans
        return dp[(setOfCities,city)]
    
    return tsp_int(1,0)

dist=[[0,20,42,25],[20,0,30,34],[42,30,0,10],[25,34,10,0]]
print(tsp(dist))