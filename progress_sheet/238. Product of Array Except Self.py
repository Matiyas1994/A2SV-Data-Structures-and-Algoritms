class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:  
        ans = []
        prepro=[1]
        
        for digits in nums:
            prepro.append(digits * prepro[-1])
        n = prepro[-1]
        
        for i in range (len(nums)):
            if nums[i] != 0:
                ans.append(int(n/nums[i]))
            else:
                ans = [0] * len(nums)
                ans[i] = prod(nums[:i]) * prod(nums[i+1:])
                return ans 
                
        return ans
           
    
    '''
        ans=[]
        for i in range(len(nums)):
            p1=0
            p2=len(nums)-1
            res=1
            while p1 < i or p2 > i:
                if p1 < i and p2 > i:
                    res= res * nums[p1] *nums[p2]
                    p1 +=1
                    p2 -= 1
                elif p1 < i:
                    res= res * nums[p1]
                    p1 +=1
                else:
                    res= res *nums[p2]
                    p2 -= 1
            ans.append(res)
               
        return ans
        '''
       
