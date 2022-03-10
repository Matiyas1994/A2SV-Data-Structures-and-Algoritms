class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        m , n = map(len,(grid,grid[0]))
        
        queue = deque()
        visited  = set()
        
        for j in range(n):
            if grid[0][j] == 1:
                queue.append((0,j))
                grid[0][j] = 0
            if grid[-1][j] == 1:
                queue.append((m-1,j))
                grid[-1][j] = 0
        for i in range(1,m-1):
            if grid[i][0] == 1:
                queue.append((i,0))
                grid[i][0] = 0
            if grid[i][-1] ==1:
                queue.append((i,n-1))
                grid[i][-1] =0
        
        neighbours =[(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            i , j = queue.popleft()
            
            for r,c in neighbours:
                newRow, newCol = i + r, j + c
            
                if 0 <= newRow <m and 0<= newCol < n and  grid[newRow][newCol]==1:
                    queue.append((newRow,newCol))
                    grid[newRow][newCol] = 0
            
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count +=1
        return count
        
        
