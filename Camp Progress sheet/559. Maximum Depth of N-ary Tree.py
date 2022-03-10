"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        def dfs(r):
            M = 0            
            if not r:
                return 0
            if len(r.children) == 0:
                return 1
            
            for c in r.children:
                M = max(M,dfs(c))
                
            return M+1
        
        return dfs(root)
