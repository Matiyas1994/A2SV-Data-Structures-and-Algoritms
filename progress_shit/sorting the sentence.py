class Solution:
    def sortSentence(self, s: str) -> str:
        res=s.split()
        new=sorted(res,key=lambda res: int(res[-1]))
        new2=[]
        for i in new:
                new2.append(i[:-1])        
        s2=" ".join(new2)
        
        return s2

        
                
