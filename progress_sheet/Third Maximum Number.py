class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        '''
        time-O(nlogn)//sorting is the bottle neck // space-O(n)
        '''
        s=sorted(list(set(nums)))
        if len(s)>=3:
            return s[-3]
        else:
            return s[-1]
