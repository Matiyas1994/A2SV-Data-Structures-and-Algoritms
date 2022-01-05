class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0 or len(nums)==1:
            return len(nums)
    
        k=0
        for i in range(len(nums)-1):
            if nums[i]!=nums[i+1]:
                nums[k] = nums[i]
                k+=1                  
        
        nums[k] = nums[len(nums)-1] 
        k+=1
        print(nums)
        return k
           
