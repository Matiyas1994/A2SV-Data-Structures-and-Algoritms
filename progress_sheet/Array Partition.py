class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
         '''
        time-O(nlogn)  space-O(1)
        '''
        nums.sort()
        sum=0
        for i in range(0,len(nums),+2):
            sum+=nums[i]
        return sum
