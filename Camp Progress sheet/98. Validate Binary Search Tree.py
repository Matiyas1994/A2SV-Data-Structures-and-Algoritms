# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       
        def valid(r):
            if not r:
                return (True,float(-inf),float(inf)
        
                        
            if not r.left and not r.right:
                return (True,r.val,r.val)
            
            l = valid(r.left)
            r2 = valid(r.right)
            
            if l[0] and r2[0]:   
                if l[1] < r.val and r2[2] > r.val:
                    return (True,max(r2[1],r.val),min(l[2],r.val))
                            
            return (False,0,0)1
            
        return valid(root)[0]
            
