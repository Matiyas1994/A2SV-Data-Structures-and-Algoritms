# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        leftmost = root.val
        hmax = float(-inf) 
        def dfs(root,h):
            nonlocal hmax,leftmost
            if not root:
                return 
            
            if h > hmax:
                leftmost = root.val
                hmax = h
                
            dfs(root.left,h+1)
            dfs(root.right,h+1)
            
            return 
        dfs(root,0)
        
        return leftmost

            
        
