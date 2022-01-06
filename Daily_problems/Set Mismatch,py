class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        from collections import Counter
        res=[]
        nums.sort()
        compare=[i for i in range(1,len(nums)+1)]
        c=Counter(nums)
        for i, val in c.items():
            if val > 1:
                res.append(i)
        for i in compare:
            if i not in nums:
                res.append(i)
        return res
