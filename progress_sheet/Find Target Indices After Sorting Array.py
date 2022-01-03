class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res=[]
        for i , val in enumerate(nums):
            if val==target:
                res.append(i)
        return res
