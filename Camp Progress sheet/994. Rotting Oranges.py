class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        number_of_one = 0
        m , n = map(len,(grid,grid[0])) 
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    number_of_one +=1
        
        
        neighbours =[(1,0),(-1,0),(0,1),(0,-1)]
        Minute = 0
        while queue:
            qulen = len(queue)
            Found = False
            for _ in range(qulen):
                row ,col = queue.popleft()
                
                for r , c in neighbours:
                    new_row = row + r
                    new_col =  col + c
                    if 0 <= new_row < m and 0<=new_col<n and grid[new_row][new_col] == 1:
                        queue.append((new_row,new_col))
                        grid[new_row][new_col] = 2
                        number_of_one -=1
                        Found =True
            if Found:
                Minute +=1
        
        if number_of_one:
            return -1
        
        return Minute 
        
                    
        
