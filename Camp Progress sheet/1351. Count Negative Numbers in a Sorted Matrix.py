class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
       
        def bs(newlist):
            left = 0
            right = len(newlist)
         
            while left < right:
                mid = (left + right)//2
                
                if newlist[mid] < 0:
                    right = mid   
                else:
                    left = mid + 1
                                 
            return right
      
        ans = 0
        for row in grid: 
            ans += len(row) - bs(row)
        
        return ans
        
        
        
