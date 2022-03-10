class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        '''
        1,get hight difference
        2, we use all lader in order 
        3, we brick for the min ones.
        4, when no brick and lader enough brick
        '''
        h_dif = []
        for i in range(len(heights)-1):
            h_dif.append(heights[i+1] - heights[i])
        
        min_dif = []
        cur = 0
        while ladders and cur < len(h_dif):
            if h_dif[cur] > 0:
                ladders -=1
                heappush(min_dif,h_dif[cur])
            cur +=1
            
        while cur < len(h_dif):
            if h_dif[cur] > 0:
                if min_dif and min_dif[0] <= h_dif[cur]:
                    if bricks >= min_dif[0]:
                        bricks -= heappop(min_dif)
                        heappush(min_dif, h_dif[cur])
                    else:
                        return cur
                else:
                    if bricks >= h_dif[cur]:
                        bricks -= h_dif[cur]
                    else:
                        return cur
            cur +=1
        
        return cur
