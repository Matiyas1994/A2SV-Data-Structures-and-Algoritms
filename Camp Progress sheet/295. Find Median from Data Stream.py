class MedianFinder:

    def __init__(self):
        self.right = []
        self.left = []
        
    def addNum(self, num: int) -> None:
        
        if len(self.left) > len(self.right):
            t=heapq.heappushpop(self.left,-num)
            heapq.heappush(self.right,-t)
        else:
            t=heapq.heappushpop(self.right,num)
            heapq.heappush(self.left,-t)
            
      
    def findMedian(self) -> float:
        
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
