"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:       
        g={}
        for em in employees:
            g[em.id] = em

        res = 0
        visited = set()
        queue =deque()
        
        if id not in g:
            return 0

        queue.append(g[id])
        while queue:
            r = queue.popleft()
            visited.add(r)
            res += r.importance
            for s in r.subordinates:
                if g[s] not in visited:
                    queue.append(g[s])
            
        return res
        
 
