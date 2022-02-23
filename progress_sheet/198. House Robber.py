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
        
        Maxrobery = [0,nums[0]]
        
        for i in range(1,len(nums)):
            Maxrobery.append (max(Maxrobery[i],Maxrobery[i-1] + nums[i]))
            
        return Maxrobery[len(nums)]
