class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        Myhash = {0:1}
        presum = [0]
        ans =0
        
        for num in nums:
            presum.append(presum[-1]+num)
            
            if presum[-1] - k in Myhash:
                ans += Myhash[presum[-1]-k]
            
            if presum[-1] in Myhash:
                Myhash[presum[-1]] +=1
                
            else:
                Myhash[presum[-1]] =1 
        
        return ans
        
        
        '''
        p1 = 0
        p2 = 0
        presum = [0]
        ans = 0
        
        if k == 0:
            presum.append(nums[0])
            p1 = 1
        
        while p1 <= len(nums)-1:
            if nums[p1] == k:
                ans += 1
                p1 += 1
            elif nums[p1] > k:
                p1 +=1
                presum.append(0)
            
            else:
                p2 = p1
                
                while p2 <= len(nums)-1 and presum[-1] < k: 
                    presum.append(presum[-1]+nums[p2])
                    p2 +=1
                    
                if presum[-1] == k:
                    ans +=1
                    
            
                presum.append(0)    
                p1 +=1
                
        return ans
        '''
        
