class RecentCounter:
    '''
    time O(1)
    space O(n)  
    '''
    def __init__(self):
        self.requests=[]
        self.count=0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while t-3000 > self.requests[0] :
            self.requests.pop(0)
        return len(self.requests)
            
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
