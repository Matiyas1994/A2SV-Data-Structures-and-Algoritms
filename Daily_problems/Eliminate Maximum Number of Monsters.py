class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time=[dist[i]/speed[i] for i in range(len(dist))]
        time.sort()
        count=0
        t=0
        
        for i in time:
            if i<= t:
                break
            else:
                t+=1
                count+=1
        return count
