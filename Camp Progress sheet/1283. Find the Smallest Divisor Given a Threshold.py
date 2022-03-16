class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        
        def answergiver(n):
            nonlocal threshold
            s = 0
            for i in nums:
                s +=ceil(i/n)
                
            if s <= threshold:
                return True
            return False
        
        
        left = 1
        right = max(nums)

        while left < right:

            mid = (right + left) //2

            if  answergiver(mid): 
                right = mid  
            else:
                left = mid + 1 

        return right
        
