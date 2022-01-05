class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        res=[]
        for i in intervals:
            if len(res)==0 or res[-1][-1] < i[0]:
                res.append(i)
            else:
                res[-1][-1]= max(res[-1][-1],i[1])
                
        return res
