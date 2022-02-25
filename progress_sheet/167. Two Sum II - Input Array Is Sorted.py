class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans= []
        p1 = 0
        p2 = len(numbers) - 1
        
        while p1 < p2:
            if numbers[p1] + numbers[p2] == target:
                ans.append(p1 +1 )
                ans.append(p2 + 1 )
                return ans
            elif numbers[p1] + numbers[p2] > target:
                p2 -=1
            else:
                p1 +=1
        
