class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time=[round(dist[i]/speed[i],2) for i in range(len(dist))]
        time.sort()
        time.remove(time[0])
        count=1
        for i in range(len(time)):
            time[i]-=1
        if len(time)!=0 and time[0] >0:
            islive=True
        else:
            islive=False
        while islive:
            if len(time)!=0 and time[0] >0:
                time.remove(time[0])
                for i in range(len(time)):
                    time[i]-=1 
                count +=1
            else: 
                islive=False
        return count
            
       
