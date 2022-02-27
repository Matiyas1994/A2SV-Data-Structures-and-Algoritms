class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
    
        p1 = 0
        p2 = 0
        Max = float(-inf)
        
        while p2 <= len(s)-1:
            Myhash=set()
            while p2 <= len(s)-1 and s[p2] not in Myhash:
                Myhash.add(s[p2])
                p2 +=1
            Max = max(Max,p2-p1)
            p1 +=1
            p2 = p1
        
        return Max
            
