class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = [[0 for j in range(len(grid[0]))] for i in range(len(grid))]
        memo[-1][-1]=grid[-1][-1]
        
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[0])-1,-1,-1):
                if  i == len(grid)-1 and  j== len(grid[0])-1:
                    continue
                if i == len(grid)-1:
                     memo[i][j] =  grid[i][j] + memo[i][j+1]
                elif j == len(grid[0])-1:
                     memo[i][j] =  grid[i][j] + memo[i+1][j]
                else:
                    memo[i][j] = grid[i][j] + min(memo[i][j+1],memo[i+1][j])
       
        return memo[0][0]
