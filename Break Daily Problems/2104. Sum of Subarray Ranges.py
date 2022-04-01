class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        Sum = 0
        
        for i in range(len(nums)):
            Max = nums[i] 
            Min = nums[i]
            
            for j in range(i,len(nums)):
                Max = max(Max,nums[j])
                Min = min(Min,nums[j])
                
                Sum += Max - Min 
        
        return Sum
        
