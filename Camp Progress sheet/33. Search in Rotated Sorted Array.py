class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(left,right):
            nonlocal target
            
            while left <= right:
                mid = (left + right)//2
                
                if nums[mid] == target:
                    return mid
                
                elif nums[mid] > target:
                    right = mid - 1
                    
                else:
                    left = mid + 1
                
            return -1
    

        smallest = nums[-1]
        if nums[0] > nums[-1]:
            r = len(nums) - 1
            l = 0
            
            while l < r:
                mid = (r + l)//2
                
                if nums[mid] > smallest:
                    l = mid + 1

                else:
                    r = mid
                    smallest = nums[mid]
            
            if target == nums[-1]:
                return len(nums) - 1
            
            elif target > nums[-1]:
                return bs(0,r)
            else:
                return bs(r,len(nums)-1)
        
        else:
            return bs(0,len(nums)-1)
        
            
