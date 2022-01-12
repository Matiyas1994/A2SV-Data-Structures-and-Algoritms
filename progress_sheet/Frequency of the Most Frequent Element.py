class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=1
        for i in range(len(nums)-1,0,-1):
            tempSum = 0
            j = i-1
            while (tempSum <= k and j>= 0):
                tempSum += nums[i]-nums[j]
                if(tempSum > k):
                    break
                res = max(res,i-j+1)  

                j -= 1
                
                
            if(res == i):
                break
        return res
        
    
