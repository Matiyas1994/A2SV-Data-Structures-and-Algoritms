class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
#         Bottom up approach
#         for i in range(len(triangle)-2,-1,-1):
#             for j in range(len(triangle[i])):
#                 triangle[i][j] += min(triangle[i+1][j],triangle[i+1][j+1])
        
#         return triangle[0][0]
        
        dp =triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j],dp[j+1])
              
        
        return dp[0]



    
    

# top down approch
    
#         memo ={}
#         def rec(i,j):
             # if i == len(triangle):
#                 return 0
#             if (i,j) in memo:
#                 return memo[(i,j)]

#             
        
#             memo[(i,j)] = triangle[i][j] + min(rec(i+1,j),rec(i+1,j+1))
#             return memo[(i,j)]
        
#         return rec(0,0)
    
