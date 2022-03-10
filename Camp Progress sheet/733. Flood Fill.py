class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        neighbors = [(1,0),(-1,0),(0,1),(0,-1)]
        m , n = map(len,(image,image[0]))    
        val = image[sr][sc]
    
        visited =set()
        
        def dfs(r,c):
            visited.add((r,c))
            image[r][c] = newColor
            for row , col in neighbors:
                cr ,ccol = r+row , col+c
                if 0 <= cr < m and 0<= ccol < n:                    
                    if  image[cr][ccol] == val and (cr,ccol) not in visited :
                        dfs(cr,ccol)
        dfs(sr,sc)
        return image   
                        
        
