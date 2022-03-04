class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c= Counter(nums)
        heap= [(value,key)for key,value in c.items()]
    
        heapq.heapify(heap)
        
        ans = heapq.nlargest(k,heap)
        return [a[1] for a in ans]
        
