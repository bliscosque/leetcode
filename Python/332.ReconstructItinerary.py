from typing import List
from collections import defaultdict
class Solution:
    
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph=defaultdict(list)
        for orig,dst in tickets:
            graph[orig].append(dst)
        for v in graph.values():
            v.sort()

        #Caminho Euler, iniciando de JFK - Alg de Hierholzer
        def find_next_path(vertex):
            path = [vertex]
            current_v = vertex
            
            while True:
                if not graph[current_v]:
                    return path
                
                next_v = graph[current_v][0]
                graph[current_v].remove(next_v)
                
                current_v = next_v
                path.append(current_v)
        
        final_path = []
        stack = ["JFK"]
        
        while stack:
            current_vertex = stack[-1]
            
            if graph[current_vertex]:
                new_path = find_next_path(current_vertex)
                stack.extend(new_path[1:])
            else:
                final_path.append(stack.pop())
        
        return final_path[::-1]



s=Solution()
print(s.findItinerary(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
print(s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))