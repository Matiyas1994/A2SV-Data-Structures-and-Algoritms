
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        int_nums=list(map(int,nums))
        int_nums.sort()
        return str(int_nums[-k])
