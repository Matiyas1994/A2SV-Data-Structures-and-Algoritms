# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def foo(self, r, t, s):        
        if not r:
            return 
        
        s += r.val
        if r.left == None and r.right==None:
            if s == t:
                return True
            else:
                return False
            
        else:
            r1 =self.foo(r.left,t,s)
            r2 =self.foo(r.right,t,s)
    
            return r1 or r2
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
       
        return self.foo(root,targetSum,0)
            
