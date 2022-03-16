class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        bestLeft = float(inf)
        bestRight = -1
        
        def bs(isleft):
            nonlocal target , bestLeft , bestRight
            left = 0
            right =  len(nums) - 1
            found = False
            while left <= right:
                mid = (left + right)//2
                
                if nums[mid] == target:
                    if isleft:
                        if bestLeft > mid:
                            bestLeft = mid 
                            right = mid -1
                    else:
                        if bestRight < mid:
                            bestRight = mid
                            left = mid + 1 
                    found = True
                        
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid -1
                    
            if isleft and not found:
                bestLeft = -1
            elif not found and not isleft: 
                bestRight = -1 
    

        bs(True)
        bs(False)
        
        return [bestLeft,bestRight]
        
