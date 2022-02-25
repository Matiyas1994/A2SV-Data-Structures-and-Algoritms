class Solution:
    def compress(self, chars: List[str]) -> int:
        s=""
        p1 = 0 
        p2 = 0
        
        while p2 <= len(chars)-1:
            dif=0
            while p2 <= len(chars)-1 and chars[p1] == chars[p2]:
                p2 +=1
                dif +=1
            if dif > 1:
                s += chars[p1]+ str(dif)
            else:
                s += chars[p1]
            p1=p2
        for i in range(len(s)):
            chars[i] = s[i]
            
        return len(s)
            
