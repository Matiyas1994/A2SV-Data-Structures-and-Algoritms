class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = dict()
        bigCount = 0 
        for num in nums:
            if num in counter:
                counter[num] +=1
            else:
                counter[num] = 1
                
            if counter[num] > bigCount:
                bigCount= counter[num]
                ans = num
        
        return ans 
