class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        '''
        time-O(nlogn) space-O(n)
        '''
        res=[]
        temp={}
        copy=sorted(nums)
        for i in range(len(nums)-1,-1,-1):
            temp[copy[i]]=i
        for i in nums:
                res.append(temp[i])
        return res
        
