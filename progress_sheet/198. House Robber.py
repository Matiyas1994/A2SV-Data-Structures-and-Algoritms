class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        evenSum=0
        oddSum=0
        for i in range(len(nums)):
            if i%2 == 0:
                evenSum += nums[i]
            else:
                oddSum += nums[i]
        return max(evenSum,oddSum)
        '''
        
        dp = [0,nums[0]]
        
        for i in range(1,len(nums)):
            dp.append (max(dp[i],dp[i-1] + nums[i]))
            
        return dp[len(nums)]
