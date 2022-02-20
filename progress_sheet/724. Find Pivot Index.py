class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumKeeper = [0]
        
        for digit in nums:
            sumKeeper.append(sumKeeper[-1]+digit)
        last = sumKeeper[-1]
        
        for i in range(len(sumKeeper)-1):
            if sumKeeper[i] == last - sumKeeper[i+1]:
                return i
        return -1
        
        
