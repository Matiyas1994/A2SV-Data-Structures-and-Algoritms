# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        inordervalue = []
        incorects =[]
        
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            inordervalue.append(root.val)
            inorder(root.right)
        
        inorder(root)
        correct = sorted(inordervalue)
        
        for i in range(len(correct)):
            if inordervalue[i] !=  correct[i]:
                incorects.append(inordervalue[i])
                incorects.append(correct[i])
                break
                
        def correcting(root):
            if not root:
                return 
            
            if root.val == incorects[0]:
                root.val = incorects[1]
            elif root.val == incorects[1]:
                root.val = incorects[0]
            
            correcting(root.left)
            correcting(root.right)
          
        correcting(root)
            
        
