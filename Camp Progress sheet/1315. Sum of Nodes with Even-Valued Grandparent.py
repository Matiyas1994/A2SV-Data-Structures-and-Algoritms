# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        res =0
        def foo(root,parent,grandpa):
            nonlocal res
            if not root:
                return
            
            if grandpa%2==0:
                res +=root.val
            
            foo(root.left,root.val,parent)
            foo(root.right,root.val,parent)
        
        foo(root,-1,-1)
        return res
