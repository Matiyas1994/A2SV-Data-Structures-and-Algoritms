class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = map(len,(grid,grid[0]))
        
        def bfs(row,col):
            nonlocal m,n
            neigh=[(1,0),(-1,0),(0,1),(0,-1)]
            queue = deque()
            queue.append((row,col))
            
            while queue:
                row , col =queue.popleft()
                grid[row][col] = "0"
                
                for  i ,j in neigh:
                    cr ,ccol = row + i , col + j
                    if 0 <= cr < m and 0 <= ccol <n and grid[cr][ccol]=="1":
                            queue.append((cr,ccol))
                            grid[cr][ccol] = "0"
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] =="1":
                    bfs(i,j)
                    res +=1
    
        return res
            
        
        
        
