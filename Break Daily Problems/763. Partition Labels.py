class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counte = Counter(s)
        ans = []
        visited=set()
        p=0
        prev = 0
        while p < len(s):
            size = counte[s[p]]
            visited.add(s[p])
            while  p < len(s) and size > 0:
                if s[p] not in visited:
                    size += counte[s[p]]-1
                    visited.add(s[p])
                else:
                    size -=1
                    
                p +=1
                
            ans.append(p-prev)
            prev = p
            
        return ans
                
     
