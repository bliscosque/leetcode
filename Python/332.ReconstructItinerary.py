from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #Caminho Euler, iniciando de JFK - Alg de Hierholzer




s=Solution()
print(s.findItinerary(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))