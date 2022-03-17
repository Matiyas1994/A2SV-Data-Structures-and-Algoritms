class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def bs(nums):
            
            left , right = 0 , len(nums)-1
            
            nonlocal target
            
            while left <= right:
                mid = (left + right)//2
                
                if nums[mid] == target:
                    return True
                
                elif nums[mid] > target:
                    right = mid - 1
                    
                else:
                    left = mid + 1
                
            return False
    
       
        if target > matrix[-1][-1] or matrix[0][0] > target:
            return False
        
      
        left = 0
        right = len(matrix) 
        
        while left < right:
            mid = (left + right)//2
            
            if matrix[mid][0] > target:
                right = mid  
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                return True
        
        
        return bs(matrix[right-1]) 
                
