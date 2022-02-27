class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
                
        presum = [0]
        Myhash = {0:1}
        ans = 0
        
        for num in nums:
            presum.append(presum[-1]+num)
            
            if presum[-1] - k in Myhash:
                ans += Myhash[presum[-1] - k]
            
            if presum[-1] in Myhash:
                Myhash[presum[-1]] +=1
            
            else:
                Myhash[presum[-1]] = 1
    
        return ans
        
        
      
