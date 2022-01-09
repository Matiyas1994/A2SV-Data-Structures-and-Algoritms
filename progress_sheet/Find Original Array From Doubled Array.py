class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2: return []
        
        count = Counter(changed)
        ans = []
        
        for num in sorted(changed):
            if count[num] == 0: continue
                
            if count[num*2] == 0: return []
        
            count[num] -= 1
            count[num*2] -= 1
            ans.append(num)
            
        return ans   
