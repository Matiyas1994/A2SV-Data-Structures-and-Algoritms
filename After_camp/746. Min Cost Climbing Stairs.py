 class Solution:
 def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache={}
        cost.append(0)
        def dp(index):
            if index in cache:
                return cache[index]
   
            if index < 2:
                return cost[index]
            
            cache[index]= cost[index] + min(dp(index-1),dp(index-2))
            
            return cache[index]
        
        return dp(len(cost)-1)
