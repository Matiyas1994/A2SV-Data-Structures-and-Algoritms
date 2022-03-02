# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.totalSum = 0
        
        if not root.left and not root.right:
            return 0
        
        def sumOfLeftLeaves(r,isleft):
            if not r:
                return 
            
            if not r.left and not r.right and isleft:
                self.totalSum += r.val
                return
            
            sumOfLeftLeaves(r.left,True)
            sumOfLeftLeaves(r.right,False)
         
        
        
        sumOfLeftLeaves(root,True)
        return self.totalSum
            
