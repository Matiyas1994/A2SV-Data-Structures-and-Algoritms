class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        import numpy as np
        median=np.median(nums)
        less=[]
        more=[]
        for j in nums:
            if j  < median:
                less.append(j)
            else:
                more.append(j))
        res=list(chain.from_iterable(zip(more,less)))
        res.extend(more[more.index(res[-2])+1:])
        return res
