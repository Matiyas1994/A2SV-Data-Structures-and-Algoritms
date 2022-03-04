class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
     
        wordsdict = Counter(words)
        
        heap = [(-freq,word) for word, freq in wordsdict.items()]
        
        heapq.heapify(heap)
        
        return [heapq.heappop(heap)[1] for _ in range(k)]

        
        
