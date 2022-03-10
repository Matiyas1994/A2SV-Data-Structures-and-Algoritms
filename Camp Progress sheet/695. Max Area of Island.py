class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        Maxarea = 0
        neighbour = [(1,0),(-1,0),(0,1),(0,-1)]
        row , col =map(len,(grid,grid[0]))
        visited = set() 
        
        def foo(i,j):
            nonlocal row, col, area
            visited.add((i,j))
            area +=1
            for r,c in  neighbour:
                new_row , new_col = i+r , j+c
                
                if 0 <= new_row < row and 0<= new_col < col and (new_row,new_col) not in visited and grid[new_row][new_col]==1:           
                    foo(new_row,new_col)
                    
                    
 
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] not in visited and grid[i][j]==1:
                    foo(i,j)
                    Maxarea = max(Maxarea,area)
                    area = 0
                    
        return Maxarea
