class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def posibility(t):
            nonlocal  totalTrips
            trips = 0
            for times in time:
                trips += t//times
                
            if trips >=  totalTrips:
                return True
            
            return False
        
        
        if len(time)==1:
            return time[0] * totalTrips
        
        left = 1
        right = sum(time) * totalTrips
        
        while left < right:
            mid = (left + right)//2
            
            if posibility(mid):
                right = mid
            else:
                left = mid + 1
                
        return right
        
            
        
