class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def possible(n):
            p = 0
            day = 0
            nonlocal days
            while  p < len(weights):
                s = 0
                while p < len(weights) and s < n:
                    s += weights[p]
                    if s <=n:
                        p +=1
                day +=1
                
            if day <= days:
                return True
            return False
    
  
        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = (left + right)//2
            
            if possible(mid):
                right = mid
            else:
                left = mid + 1
        
        return right
    
