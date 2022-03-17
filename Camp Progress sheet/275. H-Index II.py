class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n= len(citations)
        left = 0
        right = n - 1
        
        maximum = float(-inf)
        
        while left <= right:
            mid = (right - left)//2 + left
            
            if citations[mid] <= n - mid:
                left = mid + 1
                maximum= max(maximum, citations[mid])
            else:
                right = mid -1
        
        return max(maximum , n - left)
            
        
