# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trav( self ,r,r2):
        
        if r == None and r2 == None:
            return True
        elif r and not r2 or r2 and not r:
            return False
        elif r.val != r2.val:
            return False
        else:
            r1 = self.trav(r.left,r2.left)
            r2 = self.trav(r.right,r2.right)
              
            return r1 and r2
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            
            return self.trav(p,q)
            
        
                
        
