class Solution:
    def rob(self, nums: List[int]) -> int:
#         dp = [0,nums[0]]
#         for i in range(1,len(nums)):
#             dp.append (max(dp[i],dp[i-1] + nums[i]))
            
#         return dp[len(nums)]
    
        memo ={}
        def roberyplaner(i):
            if i in memo:
                return memo[i]
            if i < 0:
                return 0
            memo[i]= max(roberyplaner(i-1),roberyplaner(i-2) + nums[i])
            return memo[i]
        return roberyplaner(len(nums)-1);
