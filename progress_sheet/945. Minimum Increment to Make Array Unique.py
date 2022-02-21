class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        finalres=0
        maxi=nums[0]
        for i in range(1,len(nums)):
            if nums[i] <= maxi:
                finalres += maxi -nums[i] +1
                nums[i] = maxi + 1
            maxi = nums[i]
        return finalres
        
        ''''
        nums.sort()
        Myhash = set()
        count = 0
        for digit in nums:
            if digit not in Myhash:
                Myhash.add(digit)
            else:
                while digit in Myhash:
                    count +=1
                    digit +=1
                Myhash.add(digit)
        return count
        '''
        
