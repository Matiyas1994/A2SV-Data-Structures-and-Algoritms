class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == len(nums):
            pass
        else:
            while k > len(nums):
                k = k - len(nums)  
        
        
            temp = nums[-k:]
            temp2 = nums[:len(nums)-k]


            for i in range(k):
                nums[i] = temp[i]


            for i in range (len(nums)-k):
                nums[k+i] = temp2[i]
           
