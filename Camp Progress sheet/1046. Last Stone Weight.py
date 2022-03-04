class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        
        while len(stones) >= 2:
            f = heapq._heappop_max(stones)
            s = heapq._heappop_max(stones)
            
            if f - s > 0:
                heapq.heappush(stones,f-s)
                heapq._heapify_max(stones)
        
        if stones:
            return stones[0]
        return 0
