class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return True if len(set(s))==len(set(t))==len(set(zip(s, t))) else False
