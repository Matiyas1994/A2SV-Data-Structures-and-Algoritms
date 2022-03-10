# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        tilt = 0
        def foo(r):
            nonlocal tilt
            if not r:
                return 0
            if not r.left and not r.right:
                return r.val
            l = foo(r.left)
            ri = foo(r.right)
            tilt +=abs(l-ri)
            
            return (l + ri + r.val)
        
        foo(root)
        return tilt
            
            
