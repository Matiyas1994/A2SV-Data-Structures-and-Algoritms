class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = set()         
        counter = set()
        for i in range(len(s)-9):
            if s[i:i+10] not in counter:
                counter.add([s[i:i+10]])
            else:
                ans.add(s[i:i+10])
                
        return ans
        
        
