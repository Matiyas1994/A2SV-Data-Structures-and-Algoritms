# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def trav(r1,r2):
            if r1 == None and r2 == None:
                return True
            if not r1 or not r2:
                return False
            
            if r1.val != r2.val:
                return False
            
            a1 =trav(r1.left,r2.right)
        
            a2= trav(r1.right,r2.left)
            
            return a1 and a2
        
        return trav(root.left,root.right)
    
