# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
       
        
        def cheker(r,h):
            if not r:
                return (True,h-1)
            
            
            left = cheker(r.left, h+1)
            right = cheker(r.right, h+1)
        
            if left[0] and right[0]:
                if abs(left[1]-right[1]) <=1:
                    return (True,max(left[1],right[1]))
            return (False,0,0)
        
        return cheker(root,0)[0]
        
        
