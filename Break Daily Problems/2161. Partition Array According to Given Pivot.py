class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = []
        left = []
        right = []
        equal = []
        
        for i in range(len(nums)):
            if nums[i] < pivot:
                left.append((i,nums[i]))
            elif nums[i] > pivot:
                right.append((i,nums[i]))
            else:
                equal.append(nums[i])
        
        left.sort()
        right.sort()
        
        for n in left:
            ans.append(n[1])
        for e in equal:
            ans.append(e)
        for n in right:
            ans.append(n[1])
        
        return ans
