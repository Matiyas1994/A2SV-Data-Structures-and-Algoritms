# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def lowaccistor(root,h):
            if not root:
                return (h-1,None)
                
            if not root.left and not root.right:
                return(h,root)
            
            l= lowaccistor(root.left,h+1)
            r= lowaccistor(root.right,h+1)
            
            if l[0]==r[0]:
                return (l[0],root)
        
            if l[0] >= r[0]:
                return l
            return r
            
        return  lowaccistor(root,0)[1]
