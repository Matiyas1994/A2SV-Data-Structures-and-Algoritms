class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self. counter = defaultdict(lambda:0)
        maximum = [0,0]
        self.winners = []
        
        for i in range(len(persons)):
            self.counter[persons[i]] +=1
            if maximum[1] <= self.counter[persons[i]]:
                maximum[0] = persons[i]
                maximum[1] = self.counter[persons[i]]
                
            self.winners.append((times[i],maximum[0]))
    
        
    def q(self, t: int) -> int:
        
        saved = 0
        left = 0
        right = len(self.winners) - 1
        
        while left <= right:
            mid = (left + right)//2
            
            if self.winners[mid][0] <= t:
                left = mid +1
                saved = self.winners[mid][1]
            else:
                right = mid - 1
                
        return saved
    
        
            
  
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
