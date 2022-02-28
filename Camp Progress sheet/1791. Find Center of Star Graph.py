class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        L = []

        for i in range(len(edges)):
            for j in range(2):
                L.append(edges[i][j])

        c=Counter(L)
        n= len(edges)
        
        for key, value in c.items():
            if value == n:
                return key
    
    
        
